# notes about neuroimaging using ants

1. piperdream
  + `dicom2series <sorted_MRI_dir> 0 0 <raw_subject_exam_dicom_dir>` # 0: don't empty field; 0: don't rename files
    + `dicom2series MRI/S1 0 0 raw/S1`
    + `cd raw; foreach s in *; dicom2series ../MRI/$s 0 0 $s; end`
  + `dicom2nii "none" <subject_list_file> <protocol_list_file> <output_dir> [subdir_name]`
    + `dicom2nii "none" subject.txt protocol.txt ./MRI`
2. NeuroBattery # for multimodalities
<pre>
diff --git a/scripts/run_test.sh b/scripts/run_test.sh
index 494fae8..60dc08a 100755
--- a/scripts/run_test.sh
+++ b/scripts/run_test.sh
@@ -49,5 +49,5 @@ fi
 
 ./process_t1.sh
 ./process_modalities.sh
-./warp_labels.h PEDS012 20131101
+./warp_labels.sh PEDS012 20131101`
</pre>
  + `battery_all.sh <input_subj_dir> <output_subj_dir>`
    + set template dir (ANTS_TDIR) in `battery\all.sh` first
    + install `parallel` first
    + will scan input\_subj\_dir for each subject each timepoint, and do 
      + T1: 
        + `antsCorticalThickness.sh`
          + `KellyKapowski`
      + DTI: `nii2dt.sh` and `antsNeuroimagingBattery` for DTI
      + warp_label:
3. `LabelGeometryMeasures imageDimension labelImage [intensityImage=none] [csvFile]`
  + `LabelGeometryMeasures 3 labelImage`
4. JointLabelFusion
  + `antsJointLabelFusion.sh`: used for multi-atlas segmentation with joint label fusion
6. Atlas
  + [Mindboggle Data](http://www.mindboggle.info/data.html)
  + [Mindboggle Label](http://www.mindboggle.info/faq/labels.html)

