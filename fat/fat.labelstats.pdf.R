#!/usr/bin/env Rscript

library(dplyr)
library(stringr)
library(readr)
library(ANTsR)

dirs = list.dirs(".",recursive=F)
fat.dirs = dirs[which(str_detect(dirs, "fat$"))]

overlay.dir = "0000000_fat_overlay"
dir.create(overlay.dir)

pdf(file = "0000000_fat_overlay/0000000_fat_overlay.pdf")
par(mfrow = c(2,2))
par(bg = 'black')
for (fdir in fat.dirs) {
    f0 = list.files(fdir, pattern = "*anatomy.nii.gz") 
    id = f0 %>% str_extract("^[:alnum:]*")
    idate = f0 %>% str_extract("_[:alnum:]*_") %>% str_replace_all("_", "")
    sid = paste(id, idate, sep = "_")
    i0 = list.files(fdir, pattern = "*anatomy.nii.gz", full.names = T) %>% antsImageRead(2)
    i1 = list.files(fdir, pattern = "*label.nii.gz", full.names = T) %>% antsImageRead(2)
    vol = 
	i0 %>%
	labelStats(i1) %>%
	filter(LabelValue > 0) %>%
	mutate(key = case_when(LabelValue == 1 ~ "SAT", # Subcutaneous Adipose Tissue
	    LabelValue == 2 ~ "VAT", # Visceral Adipose Tissue
	    LabelValue == 3 ~ "Soft", # Soft tissue
	    LabelValue == 4 ~ "Bone", # Bone
	    LabelValue == 5 ~ "Psoas_muscle", # Psoas muscle
	    LabelValue == 6 ~ "Back_muscle", # Back muscle
	    LabelValue == 7 ~ "Wall_muscle", # Abdominal wall muscle
	    TRUE ~ "Others")) %>%
	mutate(id = id, StudyDate = idate) %>%
        mutate(`Area (cm^2)`= Volume, `Volume (cm^3)` = Volume/2) %>%
	select(id, StudyDate, everything(), -Volume)
    
    write_csv(vol, file.path(fdir,paste0(sid,"_9stats.csv")))

    overlay.png = file.path(fdir,paste0(sid,"_9overlay.png"))
    plot(i0, window.img = c(-300, 300), colorbar = F, doCropping=F, quality=1)
    title(main = sid, col.main = "white")
    plot(i0, i1, alpha = .9, window.img = c(-300, 300), doCropping=F, quality=1)
    plot(i0, i1, alpha = .2, window.img = c(-300, 300), doCropping=F, quality=1)
    plot(0,type='n',axes=FALSE,ann=FALSE)

    #file.copy(overlay.png, overlay.dir, overwrite = T)

}

dev.off()
