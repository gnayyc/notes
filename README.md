# notes about neuroimaging using ants

1. piperdream
  + series names
    + T1: T1 MPRAGE
    + DTI: DTI.nii.gz
    + RSBOLD: BOLD rsbold.nii.gz
  + `dicom2series <sorted_MRI_dir> 0 0 <raw_subject_exam_dicom_dir>` # 0: don't empty field; 0: don't rename files
    + `dicom2series MRI/S1 0 0 raw/S1`
    + `cd raw; foreach s in *; dicom2series ../MRI/$s 0 0 $s; end`
  + `dicom2nii "none" <subject_list_file> <protocol_list_file> <data_dir> <output_dir> [subdir_name]`
    + `dicom2nii "none" subject.txt protocol.txt ./MRI ./input MRI`
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
+./warp_labels.sh PEDS012 20131101
</pre>
  + `battery_all.sh <input_subj_dir> <output_subj_dir>`
    + set template dir (ANTS\_TDIR) in `battery\all.sh` first
    + install `parallel` first
    + will scan input\_subj\_dir for each subject each timepoint, and do
      + T1:
        + [`antsCorticalThickness.sh`](https://github.com/stnava/ANTs/wiki/antsCorticalThickness-and-antsLongitudinalCorticalThickness-output)
          + `KellyKapowski` -> \_CorticalThickness.nii.gz (DiReCt)
          + To measure mean cortical thickness, measure mean value of the ROI
            + `thick.test = as.array(antsImageRead(thick.test, 3))`
	    + `mask.test = as.array(antsImageRead(mask.label.image.file, 3))`
	    + `mask.label = ifelse( mask.test == label.id, 1, 0)`
	    + `mean( thick.test[mask.label>0] )` # this is the mean thickness of the specific label
      + DTI: `nii2dt.sh` and `antsNeuroimagingBattery` for DTI
      + warp_label:
        + `antsApplyTransforms`, applied to an **input image**, transforms it according to a **reference image** and a **transform** (or a set of transforms): Transform atlas label (`PTBP_T1_AAL.nii.gz`) to subject space (`${SUBJECTID}_BrainExtractionMask.nii.gz`) using transforms (`${SUBJECTID}_TemplateToSubject1GenericAffine.mat` + `${SUBJECTID}_TemplateToSubject0Warp.nii.gz`) -> `${SUBJECTID}_aal.nii.gz`
        + `ImageMath`, `ImageMath 3 ${SUBJECTID}_aal.nii.gz m ${SUBJECTID}_aal.nii.gz ${SUBJECTID}_BrainExtractionMask.nii.gz`: applying brain mask
3. `LabelGeometryMeasures imageDimension labelImage [intensityImage=none] [csvFile]`
  + ` LabelGeometryMeasures 3 PEDS012_20131101_BrainSegmentation.nii.gz`
4. JointLabelFusion
  + `antsJointLabelFusion.sh`: used for multi-atlas segmentation with joint label fusion
5. Atlas
  + [Mindboggle Data](http://www.mindboggle.info/data.html)
  + [Mindboggle Label](http://www.mindboggle.info/faq/labels.html)
6. Registration
  + `antsRegistrationSyN.sh -d 3 -o <ID> -f <fixed_img.nii.gz> -m <moving_img.nii.gz> -t bo -s 26`
  + antsRegistrationSyN.sh uses CC metric (slower) and antsRegistrationSyNQuick.sh uses MI
7. rsfMRI
  + `melodic --report -v -i BOLD_rsbold.nii.gz -m BOLD_brainmask.nii.gz`
  + rsbold = ANTsR::antsBOLDNetworkAnalysis()
    + ANTsR::heatmap(rsbold$mynetwork$corrmat)
8. TBSS
  + FSL
    + `tbss_1_preproc`
      + Erode FA_i slightly; zero the end slices
    + `tbss_2_reg`
      + Nonlinear registration to a target (template FMRIB58_FA or specific subject)
    + `tbss_3_postreg`
      + apply transform to target space
    + `tbss_4_prestats`
      + threshold mean FA skeleton image (0.2)
    + `design_ttest2 design 7 11`
    + Summary: Do stats in (FA -> template) space
  + camino
    + dt.nii.gz: contains the 8 components normally produced by dtfit
  + mrtrix 3
  + [ANTS](https://sourceforge.net/p/advants/discussion/840261/thread/e6fc9a8c/?limit=25)
    + [Local circularity in VBA](http://www.ncbi.nlm.nih.gov/pubmed/23151955)
      + FA_i -> T1_i normalization
      + The idea is, to maintain independence between the features used in normalization and in hypothesis testing
      + The features that drive the minimization of a similarity metric should be independent of the features that will be used in hypothesis testing.
      + eg. one should avoid combining the `SSD` and `Demons` metrics for normalization with Student's t test for assessing image-derived differences.
      + Local circularity will increase Type 1 errors (false positive rate)
    + [To prevent Local circularity in VBA](https://sourceforge.net/p/advants/discussion/840261/thread/dbfe8da5/)
      + Build T1<sub>n</sub> template using T1<sub>i</sub>, get Transform<sub>i->n</sub>
      + Normalize FA<sub>i</sub> to T1<sub>i</sub> space, and to T1<sub>n</sub> template space
      + Do stats at warped FA<sub>i</sub> in T1<sub>n</sub> template space
      + Summary: Do stats in (FA<sub>i</sub> -> T1<sub>i</sub> -> T1<sub>n</sub>) space
    + mapping:
      + `for faImage in faImages*nii.gz do
		    antsApplyTransforms .... -i faImage -o faImageWarped -t
			faImageWarp.nii.gz -t faImage0GenericAffine.mat -r faTemplate
		done`
    + skel.sh:
`AverageImages 3 averageFA.nii.gz 0 *fa.nii.gz`
then call skel.sh on averageFA.nii.gz

`ThresholdImage 3 id002_TransformationMNI.nii.gz wm.nii.gz 0.25 Inf`
`SmoothImage 3 wm.nii.gz 1 wms.nii.gz`
`ThresholdImage 3 wms.nii.gz wm.nii.gz 0.25 Inf`
`skel.sh wm.nii.gz wm_skel 1`
`snap -g wm.nii.gz -s wm_skel_topo_skel.nii.gz`
    + [bigLMstats](https://github.com/stnava/ANTsTutorial/blob/master/src/phantomMorphometryStudy.Rmd)
  + ImageMath
    + `ImageMath 3 $ref m $anat $mask`: ref used for MOCO options: b0, meanDWI, medianDWI
    + `ResampleImageBySpacing 3 $ref $ref 2.0 2.0 2.0`
    + `dt_template.nii.gz`: dt in template space
    + `ImageMath 3 fa_template.nii.gz TensorFA dt_template.nii.gz`
    + `ImageMath 3 md_template.nii.gz TensorMeanDiffusion dt_template.nii.gz`
    + `ImageMath 3 ad_template.nii.gz TensorAxialDiffusion dt_template.nii.gz`
    + `ImageMath 3 rd_template.nii.gz TensorRadialDiffusion dt_template.nii.gz`
    + `ImageMath 3 l1_template.nii.gz TensorEigenvalue dt_template.nii.gz 2` = ad_template.nii.gz
    + `ImageMath 3 l2_template.nii.gz TensorEigenvalue dt_template.nii.gz 1`
    + `ImageMath 3 l3_template.nii.gz TensorEigenvalue dt_template.nii.gz 0`

    + `ImageMath 3 fa_template.nii.gz m fa_template.nii.gz $mask_template`

9. Building Template
  + `antsMultivariateTemplateConstruction.sh` to build template image. (about 2+ days for 100+ subjects with 10 cores)
  + `antsMultivariateTemplateConstruction.sh` uses `ANTS`; `antsMultivariateTemplateConstruction2.sh` uses `antsRegistration`
  + `antsJointLabelFusion.sh` to jointly fuse the labels into template space.
    + template image T1<sub>n</sub> from T1<sub>i</sub> (produced by `antsMultivariateTemplateConstruction.sh`)
    + labels in each T1<sub>i</sub>
10. VBM pipeline
  + `antsMultivariateTemplateConstruction2.sh`: Build study specific template
  + `antsCorticalThickness.sh`: T1/MM normalization
  + Use warped images for VBM
11. Jacobian
  + the log jacobian transforms jacobian values > 1 to > 0 and values < 1 to < 0
  + [geodesic shooting (Ashburner & Friston Neuroimage 2011)](https://sourceforge.net/p/advants/discussion/840260/thread/88f73dee/)
<pre>
looks like you need two images to estimate this ... let me accentuate estimate.
image 1 is the jacobian of the transformation:
CreateJacobianDeterminantImage
​image 2 is the difference between the transformed image and the template
you can compute this (in ANTsR) via:
template = antsImageRead("template.nii.gz")
jimg = createJacobianDeterminantImage( template, fileNameOfWarp )
dimg = template - antsImageRead("warpedImage.nii.gz")
​scalarmom = dimg * jimg
i might have a sign error but this should get you close to what you want.
</pre>
12. To create a probability mask
  + `SmoothImage 3 $mask 1.0 $probabilityMask 1`
