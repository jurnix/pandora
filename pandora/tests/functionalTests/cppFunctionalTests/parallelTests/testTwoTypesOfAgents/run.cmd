#!/bin/bash
# @ job_name         = testTwoTypesOfAgents
# @ initialdir       = .
# @ output           = testTwoTypesOfAgents.log
# @ error            = testTwoTypesOfAgents.err
# @ total_tasks      = 4
# @ cpus_per_task    = 4
# @ tracing          = 0
# @ wall_clock_limit = 00:02:00

date
srun  ./testTwoTypesOfAgents
date
