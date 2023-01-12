library(baseballr) 
library (tidyverse)  
library(tRead) 
library(Lahman)
library(dplyr)


#load in 2022 data 
data <- load_seasons(2022)  
data2022 <- read.csv("/Users/emiliomartinez/Desktop/code/Data/Savant/2022savant.csv") %>% 
  mutate(pfx_x_in = -12*pfx_x, 
       pfx_z_in = 12*pfx_z)

#write equations for variables, and finally create a VAA column and round it to 2 decimal places
data_with_vaa <- data2022 %>% 
  mutate(vy_f = (-1* (sqrt((vy0^2) - (2 * ay * (50-(17/12)))))), t = ((vy_f-vy0)/ay), vz_f = vz0 + (az * t), VAA = -1 * atan(vz_f/vy_f)*(180/pi)) %>% 
  mutate(VAA = format(round(VAA, 2),nsmall = 2))



### 
# The add_vertical_approach_angle(df) function calculates vertical approach angle for a pitch and adds a VAA column to the df
# the df takes needs at least vy0 and ay initially then creates variables from those two points
# 
#
#
# 
###
add_vertical_approach_angle <- function(df) { 
  vy_f <- (-1* (sqrt((df$vy0^2) - (2 * df$ay * (50-(17/12)))))) 
  t <-  ((vy_f-df$vy0)/df$ay) 
  vz_f <- df$vz0 + (df$az * t) 
  df$VAA <- -1 * atan(vz_f/vy_f)*(180/pi)
}


testdata <- data2022 %>% 
  slice_sample(n=200)


#this is to just to get random sample points and crosscheck
sample <- data_with_vaa %>% 
  slice_sample(n = 5) %>% 
  select(game_date,pitch_name, release_speed, VAA, pitcher, description,events,player_name,inning, batter,balls, strikes)
