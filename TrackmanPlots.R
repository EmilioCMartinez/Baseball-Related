library(tidyverse)  

TrackmanFile <- read.csv("")#add csv here
#drop values if missing in columns: AutoPitchType, HorzBreak, InducedVertBreak
TrackmanFile <- TrackmanFile %>% 
  filter(complete.cases(AutoPitchType, HorzBreak, InducedVertBreak))

# Calculate the means of the columns, grouped by pitch type
means_df <- TrackmanFile %>%
  group_by(AutoPitchType) %>%
  summarise(
    avg_HorzBreak = mean(HorzBreak),
    avg_InducedVertBreak = mean(InducedVertBreak)
  )

#create colors for each pitch type
sc_colors <- c(
  "Four-Seam" = "#D22D49",
  "Sinker" = "#FE9D00",
  "Cutter" = "#933F2C",
  "Slider" = "#EEE716",
  #"ST" = "#DDB33A",
  #"SV" = "#93AFD4",
  #"KC" = "#6236CD",
  "Curveball" = "#00D1ED",
  "Splitter" = "#3BACAC",
  #"FO" = "#55CCAB",
  "Changeup" = "#1DBE3A"
)

#CREATE PLOTS FOR EVERY PITCH MOVEMENT + AVERAGE MOVMENT BY PITCH TYPE

#This is the start of the plot for every pitch
ggplot(data = TrackmanFile, aes(x = HorzBreak, y = InducedVertBreak, color = AutoPitchType)) +
  geom_point(alpha = .5, size = 3,stroke = .5) + 
  
  #add horiz/vert lines at 0,0
  geom_hline(yintercept = 0, linetype = "solid", color = "black") +
  geom_vline(xintercept = 0, linetype = "solid", color = "black") + 
  
  #Change axis to be -25:25 with grid every 10 ticks
  scale_x_continuous(breaks = seq(-25, 25, 10), limits = c(-25, 25)) +
  scale_y_continuous(breaks = seq(-25, 25, 10), limits = c(-25, 25))  +
  
  #create border around plot
  theme(panel.border = element_rect(color = "black", fill = NA, size = 1)) + 
  
  #modify legend and axes titles
  guides(fill = FALSE, color = guide_legend(title = "Pitch Type", alpha = 1)) +
  labs(title = "Movement Profile (Pitcher's Perspective)",
       x = "Horizontal Break (inches)",
       y = "Induced Vertical Break (inches)", 
       caption = "Data from Trackman") +
  theme(plot.title = element_text(face = "bold", hjust = 0.5)) +
  #this applies the sc_colors onto the AutoPitchType
  scale_color_manual(values = sc_colors) + 
  #plot for average of profiles
  geom_point(data = means_df, aes(x = avg_HorzBreak, y = avg_InducedVertBreak, color = AutoPitchType,fill = AutoPitchType), 
             size = 5, alpha = 1, shape = 21, stroke =.5, color = "black") + 
  scale_color_manual(values = sc_colors) +
  scale_fill_manual(values = sc_colors)
 
#--------------------------------------------------------

#LOCATION PLOT
strike_zone<- tibble(
  PlateLocSide = c(-0.85, -0.85, 0.85, 0.85, -0.85),
  PlateLocHeight = c(1.6, 3.5, 3.5, 1.6, 1.6)
)


ggplot(data = TrackmanFile, aes(x = PlateLocSide, y = PlateLocHeight, color = AutoPitchType)) +
  geom_point(alpha = 1, size = 2) + 
  scale_color_manual(values = sc_colors) +
  geom_path(data = strike_zone, color = "black", linewidth = 1.3) +
  ylim(0.5, 4.25) +
  xlim(-1.7, 1.7) +
  coord_fixed() + 
  labs(title = "Location Plot", 
       x = "Plate Side (feet)",
       y = "Plate Height (feet)", 
       caption = "Data from Trackman") +
  guides(fill = FALSE, color = guide_legend(title = "Pitch Type", alpha = 1)) +
  theme(plot.title = element_text(face = "bold", hjust = 0.5)) + 
  geom_segment(aes(x = -0.2833333, xend = -0.2833333, y = 1.6, yend = 3.5), color = "black", linetype = "dashed") + 
  geom_segment(aes(x = 0.2833333, xend = 0.2833333, y = 1.6, yend = 3.5), color = "black", linetype = "dashed") +
  geom_segment(aes(x = -0.85, xend = 0.85, y = 2.2, yend = 2.2), color = "black", linetype = "dashed") + 
  geom_segment(aes(x = -0.85, xend = 0.85, y = 2.9, yend = 2.9), color = "black", linetype = "dashed") 
#--------------------------------------------------------

# calculate means and standard deviations by pitch type
means <- aggregate(cbind(HorzBreak, InducedVertBreak) ~ AutoPitchType, data = TrackmanFile, FUN = mean)
sds <- aggregate(cbind(HorzBreak, InducedVertBreak) ~ AutoPitchType, data = TrackmanFile, FUN = sd)
means <- rename(means, x = HorzBreak, y = InducedVertBreak)
sds <- rename(sds, x = HorzBreak, y = InducedVertBreak)


ggplot(data = TrackmanFile, aes(x = HorzBreak, y = InducedVertBreak, color = AutoPitchType)) + 
  geom_point(alpha = 0.3, size = 2) +
  geom_hline(yintercept = 0, linetype = "solid", color = "black") +
  geom_vline(xintercept = 0, linetype = "solid", color = "black") + 
  scale_x_continuous(breaks = seq(-25, 25, 10), limits = c(-25, 25)) +
  scale_y_continuous(breaks = seq(-25, 25, 10), limits = c(-25, 25))  +
  theme(panel.border = element_rect(color = "black", fill = NA, size = 1)) + 
  guides(fill = FALSE, color = guide_legend(title = "Pitch Type", alpha = 1)) +
  labs(title = "Movement Profile (Pitcher's Perspective)",
       x = "Horizontal Break (inches)",
       y = "Induced Vertical Break (inches)", 
       caption = "Based on induced movement: 80% C.I.") +
  theme(plot.title = element_text(face = "bold", hjust = 0.5)) +
  scale_color_manual(values = sc_colors) +
  geom_point(data = means_df, aes(x = avg_HorzBreak, y = avg_InducedVertBreak, color = AutoPitchType,fill = AutoPitchType), 
             size = 3, alpha = 1, shape = 21, stroke =.5) + 
  scale_color_manual(values = sc_colors) +
  scale_fill_manual(values = sc_colors) +
  stat_ellipse(data = TrackmanFile, aes(x = HorzBreak, y = InducedVertBreak, fill = AutoPitchType), 
               geom = "polygon", alpha = 0.07, level = .80, type = "t", 
               params = list(x = means$x, y = means$y, 
                             height = sds$x*1.96, width = sds$y*1.96), linetype = "dashed") 

#AVG LOCATION PLOT

# calculate means and standard deviations by pitch type
means1 <- aggregate(cbind(PlateLocSide, PlateLocHeight) ~ AutoPitchType, data = TrackmanFile, FUN = mean)
sds1 <- aggregate(cbind(PlateLocSide, PlateLocHeight) ~ AutoPitchType, data = TrackmanFile, FUN = sd)
means1 <- rename(means1, x = PlateLocSide, y = PlateLocHeight)
sds1 <- rename(sds1, x = PlateLocSide, y = PlateLocHeight)

#strike zone outline
strike_zone<- tibble(
  PlateLocSide = c(-0.85, -0.85, 0.85, 0.85, -0.85),
  PlateLocHeight = c(1.6, 3.5, 3.5, 1.6, 1.6)
)


ggplot(data = TrackmanFile, aes(x = PlateLocSide, y = PlateLocHeight, color = AutoPitchType)) +
  #geom_point(alpha = .5, size = 2) + 
  scale_color_manual(values = sc_colors) +
  geom_path(data = strike_zone, color = "black", linewidth = 1.3) +
  ylim(0.5, 4.25) +
  xlim(-1.7, 1.7) +
  coord_fixed() + 
  labs(title = "Average Location Plot", 
       x = "Plate Side (feet)",
       y = "Plate Height (feet)", 
       caption = "Data from Trackman") +
  guides(fill = FALSE, color = guide_legend(title = "Pitch Type", alpha = 1)) +
  theme(plot.title = element_text(face = "bold", hjust = 0.5)) +  
  theme_classic()+
  geom_segment(aes(x = -0.2833333, xend = -0.2833333, y = 1.6, yend = 3.5), color = "black", linetype = "dashed") + 
  geom_segment(aes(x = 0.2833333, xend = 0.2833333, y = 1.6, yend = 3.5), color = "black", linetype = "dashed") +
  geom_segment(aes(x = -0.85, xend = 0.85, y = 2.2, yend = 2.2), color = "black", linetype = "dashed") + 
  geom_segment(aes(x = -0.85, xend = 0.85, y = 2.9, yend = 2.9), color = "black", linetype = "dashed") +
  scale_color_manual(values = sc_colors) +
  geom_point(data = means_df, aes(x = avg_PlateSide, y = avg_PlateHeight, color = AutoPitchType,fill = AutoPitchType), 
             size = 7, alpha = 1, shape = 21, stroke =.5) + 
  scale_color_manual(values = sc_colors) +
  scale_fill_manual(values = sc_colors) 
