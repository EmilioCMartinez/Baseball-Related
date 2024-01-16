library(tidyverse)
library(baseballr)
library(gridExtra)


force_plate_Data <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/force_plate.csv")
meta <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/metadata.csv")

force_plate_Data$resultant_rear_force <- sqrt(force_plate_Data$rear_force_x^2 + force_plate_Data$rear_force_y^2 + force_plate_Data$rear_force_z^2)
force_plate_Data$resultant_lead_force <- sqrt(force_plate_Data$lead_force_x^2 + force_plate_Data$lead_force_y^2 + force_plate_Data$lead_force_z^2)

#94.4 mph throw
pitch_2916_4_944 <- force_plate_Data %>% 
  filter(session_pitch == "2916_4")

# Reshape the data to long format for the individual forces
long_data <- pivot_longer(pitch_2916_4_944, 
                          cols = c(rear_force_x, rear_force_y, rear_force_z),
                          names_to = "force_type",
                          values_to = "force_value")
# Create a small data frame for the vertical lines
vline_data <- data.frame(
  xintercept = c(pitch_2916_4_944$pkh_time[1], pitch_2916_4_944$fp_10_time[1], pitch_2916_4_944$fp_100_time[1]),
  color = c("pkh_time", "fp_10_time", "fp_100_time")
)

# Plot for Rear Forces with vertical lines for event times (peak knee height,
#                                                          foot plant 10% and 100% bw)
p1 <- ggplot(long_data, aes(x = time, y = force_value, color = force_type)) +
  geom_line() +
  scale_color_manual(values = c("purple", "coral1", "deeppink2"),
                     labels = c("X", "Y", "Z")) +
  geom_vline(xintercept = pitch_2916_4_944$pkh_time[1], linetype = "dashed", color = "blue") +
  geom_vline(xintercept = pitch_2916_4_944$fp_10_time[1], linetype = "dashed", color = "green") +
  geom_vline(xintercept = pitch_2916_4_944$fp_100_time[1], linetype = "dashed", color = "red") +
  labs(colour = "Force Direction", title = "94.4 mph: Rear Leg Forces", x = "Time", y = "Force") +
  theme_classic()+
  theme(legend.position = "top", legend.direction = "horizontal")


p2 <- ggplot(pitch_2916_4_944, aes(x = time, y = resultant_rear_force)) +
  geom_line(color = "black") +
  geom_vline(data = vline_data, aes(xintercept = xintercept, color = color), linetype = "dashed") +
  scale_color_manual(values = c("pkh_time" = "blue", "fp_10_time" = "green", "fp_100_time" = "red"),
                     name = "Events", 
                     labels = c("pkh_time" = "PKH Time", "fp_10_time" = "FP 10 Time", "fp_100_time" = "FP 100 Time")) +
  labs(title = "94.4 mph: Resultant Rear Leg Force", x = "Time", y = "Force (N)") +
  theme_classic() +
  theme(legend.position = "bottom", legend.direction = "horizontal")


grid.arrange(p1, p2, ncol = 1)




#93.1 mph throw
pitch_2935_2_931 <- force_plate_Data %>% 
  filter(session_pitch == "2935_2")

# Reshape the data to long format for the individual forces
long_data_2 <- pivot_longer(pitch_2935_2_931, 
                          cols = c(rear_force_x, rear_force_y, rear_force_z),
                          names_to = "force_type",
                          values_to = "force_value")
# Create a small data frame for the vertical lines
vline_data2 <- data.frame(
  xintercept = c(pitch_2935_2_931$pkh_time[1], pitch_2935_2_931$fp_10_time[1], pitch_2935_2_931$fp_100_time[1]),
  color = c("pkh_time", "fp_10_time", "fp_100_time")
)

# Plot for Rear Forces with vertical lines for event times (peak knee height,
#                                                          foot plant 10% and 100% bw)
p3 <- ggplot(long_data_2, aes(x = time, y = force_value, color = force_type)) +
  geom_line() +
  scale_color_manual(values = c("purple", "coral1", "deeppink2"),
                     labels = c("X", "Y", "Z")) +
  geom_vline(xintercept = pitch_2935_2_931$pkh_time[1], linetype = "dashed", color = "blue") +
  geom_vline(xintercept = pitch_2935_2_931$fp_10_time[1], linetype = "dashed", color = "green") +
  geom_vline(xintercept = pitch_2935_2_931$fp_100_time[1], linetype = "dashed", color = "red") +
  labs(colour = "Force Direction", title = "93.1 mph: Rear Leg Forces", x = "Time", y = "Force") +
  theme_classic()+
  theme(legend.position = "top", legend.direction = "horizontal")


p4 <- ggplot(pitch_2935_2_931, aes(x = time, y = resultant_rear_force)) +
  geom_line(color = "black") +
  geom_vline(data = vline_data2, aes(xintercept = xintercept, color = color), linetype = "dashed") +
  scale_color_manual(values = c("pkh_time" = "blue", "fp_10_time" = "green", "fp_100_time" = "red"),
                     name = "Events", 
                     labels = c("pkh_time" = "PKH Time", "fp_10_time" = "FP 10 Time", "fp_100_time" = "FP 100 Time")) +
  labs(title = "93.1 mph: Resultant Rear Leg Force", x = "Time", y = "Force (N)") +
  theme_classic() +
  theme(legend.position = "bottom", legend.direction = "horizontal")


grid.arrange(p3, p4, ncol = 1)





