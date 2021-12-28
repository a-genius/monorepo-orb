#!/usr/bin/env bash

if [ ! -f "<< parameters.modules-path >>" ] || [ ! -s "<< parameters.modules-path >>" ]
then
  echo 'Nothing to merge. Halting the job.'
  circleci-agent step halt
  exit
fi

xargs -a "${MODULES_PATH}" yq -y -s 'reduce .[] as $item ({}; . * $item)' | tee "${CONTINUE_CONFIG}"
