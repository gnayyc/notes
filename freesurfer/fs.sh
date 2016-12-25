#!/bin/sh

function Usage {
    cat <<USAGE

Usage:

`basename $0` INPUT_FILE FS_SUBJ_DIR 

Examples:

    `basename $0` ./input/012345/20160610/mri/3D_T1.nii.gz ./fs.output

USAGE
    exit 0
}

# parse command line
if [ $# -ne 2 ]; then #  must be two
    Usage >&2
fi

function logCmd() {
  cmd="$*"
  echo "BEGIN >>>>>>>>>>>>>>>>>>>>"
  echo $cmd
  $cmd

  cmdExit=$?

  if [[ $cmdExit -gt 0 ]];
    then
      echo "ERROR: command exited with nonzero status $cmdExit"
      echo "Command: $cmd"
      echo
      if [[ ! $DEBUG_MODE -gt 0 ]];
        then
          exit 1
        fi
    fi

  echo "END   <<<<<<<<<<<<<<<<<<<<"
  echo
  echo

  return $cmdExit
}

IF=`realpath $1`
SD=`realpath $2`

if [ ! -d ${SD} ]; then
    mkdir -p ${SD}
fi

if [[ -f "$IF" ]]; then
    SID=`echo ${IF} | awk -F"/" '{print $(NF-3) "_" $(NF-2)}'` 
    if [[ -f ${SD}/${SID}/mri/rawavg.mgz ]]; then
	logCmd recon-all -all -sd ${SD} -s ${SID}
    else 
	logCmd recon-all -all -sd ${SD} -s ${SID} -i ${IF}
    fi
else
    echo $IF does not exist!!
fi

    SID=$1_$2
    IF=${FROM_DIR}/$1/$2/$3/$4
