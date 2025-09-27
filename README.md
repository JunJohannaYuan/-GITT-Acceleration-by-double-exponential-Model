# -GITT-Acceleration-by-double-exponential-Model
This code repository is the official implementation of the paper "Data-driven acceleration of GITT through physics-informed machine learning" (Yuan et al.). It provides a complete, end-to-end solution for significantly accelerating GITT testing and achieving high-precision simulation of battery dynamic behavior.
# About test data：
There are three dataset for different cells. Each cycle begin with a CCCV discgarge first (curreent = 0.2C mA, cut-off voltage:2.75V, cut-off current: 0.40 mA) and 2 h rest to capacity equal to zero. Then GITT charge is carried using 10min pulse at C/20 (2 mA) follwing by differnet relaxation step, when it fully charged, the GITT discharge then start.
The relaxation duration vary: 10min ,20min, 30min,40min, 50min 1h,2h and 3h 
all the dataset used in the study:  **https://zenodo.org/uploads/17201475**
**Corresponding research paper**: "Data-driven acceleration of GITT through physics-informed machine learning" (Jun Yuan, Shanling Ji et al.)

a test cycle data is provided as an example for running test: test_3_7_20C_10min10min_20250218.xlsx, and corresponding runding result for every step are given.

# About ECM coupled with FRLS and FEKF algorithms is based on the research: 
Ji, S. et al. Continuous physics-informed learning expedites universal battery mechanism decoupling. Preprint at **https://doi.org/10.26434/chemrxiv-2025-14zsv (2025)**.
**more detailed info about 2RC ECM model: https://github.com/SLJME42/2RCECM**

For questions or discussions regarding this code or the associated research, please feel free to contact Jun Yuan at: **jun.yuan@tum.de**, or Prof.Dr. Helge Stein at: **helge.stein@tum.de**
