library(tidyverse)
library(baseballr)
library(gridExtra)


force_plate_Data <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/force_plate.csv")
meta <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/metadata.csv")

force_plate_Data$resultant_rear_force <- sqrt(force_plate_Data$rear_force_x^2 + force_plate_Data$rear_force_y^2 + force_plate_Data$rear_force_z^2)
force_plate_Data$resultant_lead_force <- sqrt(force_plate_Data$lead_force_x^2 + force_plate_Data$lead_force_y^2 + force_plate_Data$lead_force_z^2)

#create a fp10 to fp100 time called delta_fp
force_plate_Data$fp_100_time[is.na(force_plate_Data$fp_100_time)] <- 0
force_plate_Data$fp_10_time[is.na(force_plate_Data$fp_10_time)] <- 0
force_plate_Data$delta_fp <- force_plate_Data$fp_100_time - force_plate_Data$fp_10_time

#add pitch speed from meta df to force plate data
force_plate_Data <- force_plate_Data %>% 
  left_join(meta %>% select(session_pitch, pitch_speed_mph), by = 'session_pitch')



#choose a pitch with a large delta_fp
pitch_2811_5_749 <- force_plate_Data %>% 
  filter(session_pitch == "2811_5")

# Reshape the data to long format for the individual forces
long_data_lead <- pivot_longer(pitch_2811_5_749, 
                          cols = c(lead_force_x, lead_force_x, lead_force_x),
                          names_to = "force_type",
                          values_to = "force_value")
# Create a small data frame for the vertical lines
vline_data_lead <- data.frame(
  xintercept = c(pitch_2811_5_749$pkh_time[1], pitch_2811_5_749$fp_10_time[1], pitch_2811_5_749$fp_100_time[1]),
  color = c("pkh_time", "fp_10_time", "fp_100_time")
)

# Plot for Rear Forces with vertical lines for event times (peak knee height,
#                                                          foot plant 10% and 100% bw)
pl1 <- ggplot(long_data_lead, aes(x = time, y = force_value, color = force_type)) +
  geom_line() +
  scale_color_manual(values = c("purple", "coral1", "deeppink2"),
                     labels = c("X", "Y", "Z")) +
  geom_vline(xintercept = pitch_2811_5_749$pkh_time[1], linetype = "dashed", color = "blue") +
  geom_vline(xintercept = pitch_2811_5_749$fp_10_time[1], linetype = "dashed", color = "green") +
  geom_vline(xintercept = pitch_2811_5_749$fp_100_time[1], linetype = "dashed", color = "red") +
  labs(colour = "Force Direction", title = "74.9 mph: Front Leg Forces", x = "Time", y = "Force") +
  theme_classic()+
  theme(legend.position = "top", legend.direction = "horizontal")


pl2 <- ggplot(pitch_2811_5_749, aes(x = time, y = resultant_lead_force)) +
  geom_line(color = "black") +
  geom_vline(data = vline_data_lead, aes(xintercept = xintercept, color = color), linetype = "dashed") +
  scale_color_manual(values = c("pkh_time" = "blue", "fp_10_time" = "green", "fp_100_time" = "red"),
                     name = "Events", 
                     labels = c("pkh_time" = "PKH Time", "fp_10_time" = "FP 10 Time", "fp_100_time" = "FP 100 Time")) +
  labs(title = "74.9 mph: Resultant Lead Leg Force", x = "Time", y = "Force (N)") +
  theme_classic() +
  theme(legend.position = "bottom", legend.direction = "horizontal")


grid.arrange(pl1, pl2, ncol = 1)


#top 10 in delta_fp (can change to longest or shortest)
leader_delta_fp<- force_plate_Data %>%
  group_by(session_pitch) %>%
  summarise(max_delta_fp = max(delta_fp)) %>%
  arrange(desc(max_delta_fp)) %>%
  slice_head(n = 10)

print(leader_delta_fp)


cor(force_plate_Data$delta_fp, force_plate_Data$resultant_rear_force, use = "complete.obs")


ggplot(force_plate_Data, aes(x = delta_fp, y = resultant_lead_force)) + geom_point()



