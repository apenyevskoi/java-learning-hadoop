#-----Preparetion code--------------------------------
library(tidyverse)
library(writexl)
library(readxl)
library(dplyr)

rm(list = ls())

setwd("C:/Users/INSAGNIFICANT/Downloads/R")

#vector of the words to count
keys = c('cogitare', 'est', 'militate', 'Scientia', 'Vivere', 'potentia',"yeqyxb","cjsxka", "itloth","jkqxpf","myithy","xgiiby")
python_100mln_lines = ''
#dataframe with 100mln rows
df1 <- data.frame(num = round(runif(100000000, 1, 12)))
#count each unique value in df1
#df1 %>% group_by(num) %>% count()

#dataframe with 100mln keys and Hadoop MapReduce's Reducer's input file to count words <Key\tValue\n>
df_100mln <- data.frame(keys = keys[df1$num], values = as.character(1))

#save to .txt file to be used in python MapReduce's Reducer function 
#1,15GB
writeLines(paste(as.character(df_100mln$keys), '\t', as.character(df_100mln$values)), 'python_100mln_lines.txt', sep = '\n')

