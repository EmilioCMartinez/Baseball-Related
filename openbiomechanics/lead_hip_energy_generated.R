library(tidyverse)
options(dplyr.width = Inf)
library(gtable)
library(gt)
library(gridExtra)
library(broom)

energy_flow <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/energy_flow.csv")
poi_metrics <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/poi_metrics.csv")
force_plate <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/force_plate.csv")
force_moments <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/forces_moments.csv")
joint_angles <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/joint_angles.csv")
joint_velos <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/joint_velos.csv")
landmarks <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/landmarks.csv")
metadata <- read_csv("/Volumes/Emilio's Ex/code/Data/OpenBiomech/Pitching/metadata.csv")



#combine metadata and poi metrics for simple plotting to start 
combined_meta_poi <- merge(metadata, poi_metrics, by = "session_pitch")
combined_meta_poi <- combined_meta_poi %>% 
  select(-c(session.x,session.y,user,filename_new,modelname_new,pitch_speed_mph.y)) %>% 
  rename(pitch_speed_mph = pitch_speed_mph.x)


mean_velocity <- mean(combined_meta_poi$pitch_speed_mph, na.rm = TRUE)
std_velocity <- sd(combined_meta_poi$pitch_speed_mph, na.rm = TRUE)

combined_meta_poi$thrower_type <- ifelse(combined_meta_poi$pitch_speed_mph > (mean_velocity + std_velocity), "Hard Thrower",
                                         ifelse(combined_meta_poi$pitch_speed_mph < (mean_velocity - std_velocity), "Soft Thrower", "Average"))

hard_throwers <- combined_meta_poi %>% 
  filter(thrower_type == "Hard Thrower")
soft_throwers <- combined_meta_poi %>% 
  filter(thrower_type == "Soft Thrower")


pitch <- energy_flow %>% 
  filter(session_pitch == "2916_2")


ggplot(pitch, aes(x = time, y = lead_hip_energy_generated)) + 
  geom_line() + 
  geom_vline(aes(xintercept = fp_10_time, color = "fp_10_time"), linetype = "solid")+
  geom_vline(aes(xintercept = fp_100_time, color = "fp_100_time"), linetype = "solid") +
  geom_vline(aes(xintercept = MER_time, color = "MER_time"), linetype = "solid") +
  geom_vline(aes(xintercept = BR_time, color = "BR_time"), linetype = "solid") +
  geom_vline(aes(xintercept = MIR_time, color = "MIR_time"), linetype = "solid") +
  labs(color = "Event") +  
  xlim(0, 1.2) + 
  ggtitle( "93.0 mph, 86.6 kg")+
  theme_classic()


energy_velo <- left_join(energy_flow,combined_meta_poi %>% select(session_pitch, pitch_speed_mph), by = "session_pitch")


