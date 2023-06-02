library(tidyverse)
library(ggforce)


twenty22 <- read_csv("/Users/emiliomartinez/Desktop/code/Data/Savant/2022savant.csv") 

swing_events <- c(
  "foul_tip", "swinging_strike", "swinging_strike_blocked", 
  "missed_bunt", "foul", "hit_into_play", "foul_bunt", "bunt_foul_tip"
)

whiff_events <- c(
  "swinging_strike", "foul_tip", "foul_bunt", 
  "missed_bunt", "swinging_strike_blocked"
)

'''hitter_names <- mlb_people(unique(mlb_data$batter)) %>%
  select(batter = id, hitter_name = last_first_name)'''


data2022 <- twenty22 %>%
  # drop any missing rows
  mutate(
    is_swing = if_else(description %in% swing_events, 1, 0), # binary indicator for a swing
    is_whiff = if_else(description %in% whiff_events, 1, 0), # binary indicator for a whiff
    is_in_zone = if_else(zone %in% 1:9, 1, 0), # binary indicator for in-zone
    is_out_zone = if_else(zone > 9, 1, 0), # binary indicator for out-of-zone
    is_chase = if_else(
      is_swing == 1 & is_out_zone == 1, 1, 0
    ), #binary indicator for swing
    is_contact = if_else(
      description %in% c("hit_into_play", "foul", "foul_pitchout"), 1, 0
    ), # binary indicator for contact
    hitting_team = if_else(
      inning_topbot == "Top", away_team, home_team
    ), # column for batting team
    pitching_team = if_else(
      inning_topbot == "Top", home_team, away_team
    ), # column for pitching team
  ) 

'''%>%
  left_join(hitter_names, by = "batter")'''

judge <- data2022 %>% 
  filter(batter == 592450) 


j <- judge %>% 
  filter(launch_speed > 97.9)

coordinates <- judge %>% 
  select(launch_speed, plate_x, plate_z,zone,bb_type,launch_angle,is_swing,is_whiff,events)
cordinates_clean <- coordinates[complete.cases(coordinates[ , c('launch_speed')]), ] 


ggplot(data = coordinates_clean, aes(x = launch_angle)) +
  geom_density(fill = "lightblue", color = "black") +
  labs(title = "Distribution of Launch Angles", x = "Launch Angle", y = "Density")


ggplot(data = cordinates_clean, aes(x = launch_angle, y = launch_speed)) +
  geom_bin2d() +
  scale_fill_gradientn(colors = c("white", "blue", "red")) +
  labs(title = "Launch Angle vs. Launch Speed Heatmap", x = "Launch Angle", y = "Launch Speed")

home_run_data <- cordinates_clean %>%
  filter(events == "home_run")

min_launch_speed <- min(home_run_data$launch_speed)
max_launch_speed <- max(home_run_data$launch_speed)
min_launch_angle <- min(home_run_data$launch_angle)
max_launch_angle <- max(home_run_data$launch_angle)
# Calculate the center and radius of the circle
circle_center <- c((min_launch_angle + max_launch_angle) / 2, (min_launch_speed + max_launch_speed) / 2)
radius <- max(max_launch_angle - min_launch_angle, max_launch_speed - min_launch_speed) / 2


# Hexbin plot
hexbin_plot <- ggplot(data = cordinates_clean, aes(x = launch_angle, y = launch_speed)) +
  geom_hex() +
  scale_fill_gradientn(colors = c("white", "blue", "red")) +
  labs(title = "Launch Angle vs. Launch Speed Hexbin Plot", x = "Launch Angle", y = "Exit Velocity") + 
  scale_x_continuous(breaks = seq(-100, 100, 50)) +  # Adjust x-axis tick marks
  scale_y_continuous(breaks = seq(-30, 120, 25)) + 
  geom_hline(yintercept = 98, linetype = "dashed", color = "black") +
  geom_vline(xintercept = c(26, 30), linetype = "dashed", color = "black")  

# Create the circle plot
circle_plot <- hexbin_plot +
  geom_circle(aes(x0 = circle_center[1], y0 = circle_center[2], r = radius),
              fill = NA, color = "Black", linewidth = 1) +
  labs(title = "Juan Soto 2022")

# Display the circle plot
circle_plot




#LOCATION PLOT
strike_zone<- tibble(
  PlateLocSide = c(-0.85, -0.85, 0.85, 0.85, -0.85),
  PlateLocHeight = c(1.6, 3.5, 3.5, 1.6, 1.6)
)

ggplot(cordinates_clean) + 
  stat_summary_hex(aes(x = plate_x, y = plate_z, z = launch_speed),binwidth = .2) + 
  scale_fill_distiller(palette = "RdBu", direction = -1) +
  geom_path(data = strike_zone, aes(x = PlateLocSide, y = PlateLocHeight), color = "black", linewidth = 1.3) + 
  geom_segment(aes(x = -0.2833333, xend = -0.2833333, y = 1.6, yend = 3.5), color = "black", linetype = "dashed") + 
  geom_segment(aes(x = 0.2833333, xend = 0.2833333, y = 1.6, yend = 3.5), color = "black", linetype = "dashed") +
  geom_segment(aes(x = -0.85, xend = 0.85, y = 2.2, yend = 2.2), color = "black", linetype = "dashed") + 
  geom_segment(aes(x = -0.85, xend = 0.85, y = 2.9, yend = 2.9), color = "black", linetype = "dashed") +
  geom_segment(aes(x = -0.708, y = 0.15, xend = 0.708, yend = 0.15), 
               size = 1, color = "black") + 
  geom_segment(aes(x = -0.708, y = 0.3, xend = -0.708, yend = 0.15), 
               size = 1, color = "black") + 
  geom_segment(aes(x = -0.708, y = 0.3, xend = 0, yend = 0.5), size = 1, 
               color = "black") + 
  geom_segment(aes(x = 0, y = 0.5, xend = 0.708, yend = 0.3), size = 1, 
               color = "black") + 
  geom_segment(aes(x = 0.708, y = 0.3, xend = 0.708, yend = 0.15), size = 1, 
               color = "black") + 
  coord_cartesian(xlim = c(-2.5, 2.5), ylim = c(0, 5))+
  labs(title = "2022 Aaron Judge Exit Velo - Catcher Perspective", 
       x = "Plate Side", y = "Plate Height",fill = "EV(mph)")

