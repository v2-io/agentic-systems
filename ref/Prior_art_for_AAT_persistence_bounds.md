# Prior art for AAT persistence bounds

##### [**Undermind**](https://undermind.ai)

---

**Research Goal:** Find academic prior art establishing scientific precedence for a theoretical framework of agency (AAT) in which agent survival or persistence is modeled as a dynamical-systems problem using Lyapunov stability. The core claim is that, rather than simple linear correction, the agent’s correction mechanism is bounded by a sector condition with efficiency alpha, and persistence requires that the correction rate exceed environmental drift divided by the agent’s reserve. The framework further claims that tracking error or mismatch scales differently depending on the disturbance class: as 1/alpha against deterministic drift and as 1/sqrt(alpha) against stochastic noise. It also claims that maintaining persistence against noise requires sustained Shannon information acquisition at a strict minimum rate, i.e. an information-rate floor. Prioritize exact mathematical equivalence wherever it exists, even if the papers are framed in different language from AAT. Also include bridge papers that translate the same mathematics into learning, cognition, viability, or agentic terms when they are clearly relevant. Relevant domains include nonlinear control theory, robust control, cybernetics, and information-theoretic control, under assumptions of agents operating in environments with persistent external disturbances such as drift or noise. Relevant matches include applications of the Lur’e problem, sector conditions, or absolute stability directly to cognitive mismatch, learning updates, or agent viability; inequalities bounding tracking error or viability against environmental drift; proofs of the specific 1/rate versus 1/sqrt(rate) tracking-error scaling dichotomy in deterministic versus stochastic environments; and proofs of a strict minimum Shannon channel capacity or information rate required for bounded tracking error, including Bode-integral-related and data-rate-theorem lineages. Exclude standard Lyapunov stability of purely physical or mechanical systems without an information or learning component, and exclude basic bandit regret bounds or stationary reinforcement learning that do not address tracking in non-stationary or drifting environments. Search across the full academic literature, including older cybernetics and control sources, with no recency restriction.

*Found 103 papers · May 21, 2026 · Estimated coverage of relevant papers: 45%*

## Summary of Results

Lyapunov- and sector-based persistence has clear prior art in two largely separate lineages: Lur’e/absolute-stability theory provides the nonlinear bounded-correction model \[1\], \[2\], while networked and information-theoretic control establishes strict minimum information rates for maintaining bounded or recurrent behavior under persistent disturbance \[3\], \[4\], \[5\], \[6\], \[7\], \[8\].

#### Mathematical backbone

- **Sector-bounded correction** is canonical in the Lur’e problem: nonlinear feedback laws constrained to a sector `{α,β}` are analyzed by Lyapunov/input-output methods, with boundedness and absolute stability derived from circle/Popov-type criteria \[1\].
- **Persistence as drift rejection** appears in input-to-state formulations for Lur’e systems, where bounded exogenous input produces bounded state/error with explicit gain-like dependence on the restoring dynamics \[2\].

#### Drift/noise scaling bridges

- **Deterministic nonstationarity** in adaptive tracking gives residual error proportional to environment change rate divided by adaptation gain/step size, i.e. the same qualitative `drift / correction-rate` law \[9\], \[10\], \[11\].
- **Stochastic disturbance** yields Ornstein–Uhlenbeck/Kalman/LMS-type steady-state RMS scaling with the inverse square root of contraction rate, rather than inverse-linear scaling; the adaptive-filter literature treats this as the core tracking-versus-noise tradeoff \[12\], \[13\], \[14\], \[15\].

#### Information-rate floor

- **A strict rate threshold** for stabilization/persistence is the data-rate theorem: required channel rate exceeds the sum of unstable growth rates \[3\], \[4\], \[5\], \[16\].
- **Noisy channels sharpen this to Shannon/anytime capacity conditions** for stochastic stability and bounded moments \[6\], \[7\], \[17\].
- **Performance-limited variants** connect disturbance attenuation and Bode-like integrals to directed-information lower bounds, bridging regulation and information acquisition costs \[18\], \[19\], \[20\].

## Paper Catalog (103 papers)

|  | Year | Cit/yr | Title | Authors | Journal |
|---:|:--:|:--:|:---|:---|:---|
| 1 | 2004 | 80 | Control under communication constraints ([link](https://doi.org/10.1109/TAC.2004.831187)) | S. Tatikonda and S. Mitter | IEEE Transactions on Automatic Control |
| 2 | 2006 | 21 | The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link—Part I: Scalar Systems ([link](https://doi.org/10.1109/TIT.2006.878169)) | Anant Sahai and S. Mitter | IEEE Transactions on Information Theory |
| 3 | 2004 | 34 | Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates ([link](https://doi.org/10.1137/S0363012902402116)) | G. Nair and R. Evans | SIAM J. Control. Optim. |
| 4 | 1999 | 34 | Systems with finite communication bandwidth constraints. II. Stabilization with limited information feedback ([link](https://doi.org/10.1109/9.763226)) | W. Wong and R. Brockett | IEEE Trans. Autom. Control. |
| 5 | 2009 | 13 | Data Rate Theorem for Stabilization Over Time-Varying Feedback Channels ([link](https://doi.org/10.1109/TAC.2008.2010887)) | Paolo Minero, M. Franceschetti, S. Dey, and G. Nair | IEEE Transactions on Automatic Control |
| 6 | 2012 | 2.6 | Characterization of Information Channels for Asymptotic Mean Stationarity and Stochastic Stability of Nonstationary/Unstable Linear Systems ([link](https://doi.org/10.1109/TIT.2012.2204033)) | S. Yüksel | IEEE Transactions on Information Theory |
| 7 | 1966 | 10 | On the input-output stability of time-varying nonlinear feedback systems–Part II: Conditions involving circles in the frequency plane and sector nonlinearities ([link](https://doi.org/10.1109/TAC.1966.1098356)) | G. Zames | IEEE Transactions on Automatic Control |
| 8 | 2008 | 15 | Feedback Control in the Presence of Noisy Channels: “Bode-Like” Fundamental Limitations of Performance ([link](https://doi.org/10.1109/TAC.2008.929361)) | N. C. Martins and M. Dahleh | IEEE Transactions on Automatic Control |
| 9 | 2000 | 65 | Quantized feedback stabilization of linear systems ([link](https://doi.org/10.1109/9.867021)) | R. Brockett and D. Liberzon | IEEE Trans. Autom. Control. |
| 10 | 2001 | 74 | Stabilization of linear systems with limited information ([link](https://doi.org/10.1109/9.948466)) | N. Elia and S. Mitter | IEEE Trans. Autom. Control. |
| 11 | 2000 | 13 | Stabilization with data-rate-limited feedback: tightest attainable bounds ([link](https://doi.org/10.1016/S0167-6911(00%2900037-2)) | G. Nair and R. Evans | Systems & Control Letters |
| 12 | 1984 | 4.2 | On the statistical efficiency of the LMS algorithm with nonstationary inputs ([link](https://doi.org/10.1109/TIT.1984.1056892)) | B. Widrow and E. Walach | IEEE Trans. Inf. Theory |
| 13 | 2006 | 1.7 | The necessity and sufficiency of anytime capacity for stabilization of a linear system over a noisy communication link, Part II: vector systems ([link](https://www.semanticscholar.org/paper/30bacce26f417f7ae9dde9ce6196870496f30f12)) | Anant Sahai and S. Mitter | arXiv: Information Theory |
| 14 | 2015 | 3.9 | Input-to-state stability of Lur’e systems ([link](https://doi.org/10.1007/S00498-015-0147-0)) | E. Sarkans and H. Logemann | Mathematics of Control, Signals, and Systems |
| 15 | 2004 | 18 | When bode meets shannon: control-oriented feedback communication schemes ([link](https://doi.org/10.1109/TAC.2004.834119)) | N. Elia | IEEE Transactions on Automatic Control |
| 16 | 1976 | 29 | Stationary and nonstationary learning characteristics of the LMS adaptive filter ([link](https://doi.org/10.1007/978-94-010-1223-2_23)) | B. Widrow, J. Mccool, M. Larimore, and C. Johnson | Proceedings of the IEEE |
| 17 | 2015 | 3.4 | Passification based synchronization of nonlinear systems under communication constraints and bounded disturbances ([link](https://doi.org/10.1016/j.automatica.2015.03.012)) | Alexander L. Fradkov, B. Andrievsky, and M. Ananyevskiy | Autom. |
| 18 | 2003 | 7.9 | On stabilization of linear systems with limited information ([link](https://doi.org/10.1109/TAC.2002.808487)) | D. Liberzon | IEEE Trans. Autom. Control. |
| 19 | 2014 | 4.6 | A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level ([link](https://doi.org/10.1109/TAC.2015.2500658)) | Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina | IEEE Transactions on Automatic Control |
| 20 | 2009 | 1.9 | Disturbance rejection with information constraints: Performance limitations of a scalar system for bounded and Gaussian disturbances ([link](https://doi.org/10.1016/j.automatica.2012.02.040)) | Hidenori Shingin and Y. Ohta | Autom. |
| 21 | 2007 | 3.6 | Shannon zero error capacity in the problems of state estimation and stabilization via noisy communication channels ([link](https://doi.org/10.1080/002071706000981775)) | A. Matveev and A. Savkin | Int. J. Control |
| 22 | 1987 | 1.7 | Nonstationary learning characteristics of the LMS algorithm ([link](https://doi.org/10.1109/TCS.1987.1086054)) | W. Gardner |  |
| 23 | 2015 | 2.1 | Stationary and Ergodic Properties of Stochastic NonLinear Systems Controlled over Communication Channels ([link](https://doi.org/10.1137/140989686)) | S. Yüksel | SIAM J. Control. Optim. |
| 24 | 1988 | 0.2 | Algebraic conditions for absolute tracking control of Lurie systems ([link](https://doi.org/10.1080/00207178808906207)) | L. Grujic | International Journal of Control |
| 25 | 2011 | 4.1 | A Framework for Control System Design Subject to Average Data-Rate Constraints ([link](https://doi.org/10.1109/TAC.2010.2098070)) | Eduardo I. Silva, M. Derpich, and Jan Østergaard | IEEE Transactions on Automatic Control |
| 26 | 1991 | 1.1 | A result on the mean square error obtained using general tracking algorithms ([link](https://doi.org/10.1002/ACS.4480050402)) | L. Ljung and P. Priouret | International Journal of Adaptive Control and Signal Processing |
| 27 | 1969 | 0.6 | The Information Transfer Required in Regulatory Processes ([link](https://doi.org/10.1109/TSSC.1969.300226)) | R. Conant | IEEE Trans. Syst. Sci. Cybern. |
| 28 | 1980 | 1.4 | Tracking properties of adaptive signal processing algorithms ([link](https://doi.org/10.1109/ICASSP.1980.1170938)) | D. Farden and K. Sayood | IEEE International Conference on Acoustics, Speech, and Signal Processing |
| 29 | 2009 | 1.6 | Synchronization of Passifiable Lurie Systems Via Limited-Capacity Communication Channel ([link](https://doi.org/10.1109/TCSI.2008.2001365)) | Alexander L. Fradkov, B. Andrievsky, and R. Evans | IEEE Transactions on Circuits and Systems I: Regular Papers |
| 30 | 2012 | 4.7 | Minimal Bit Rates and Entropy for Exponential Stabilization ([link](https://doi.org/10.1137/110829271)) | F. Colonius | SIAM J. Control. Optim. |
| 31 | 2015 | 1.1 | LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc)) | Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter | ArXiv |
| 32 | 2018 | 3.9 | Entropy and Minimal Bit Rates for State Estimation and Model Detection ([link](https://doi.org/10.1109/TAC.2017.2782478)) | D. Liberzon and S. Mitra | IEEE Transactions on Automatic Control |
| 33 | 1982 | 2.5 | A measure of the tracking capability of recursive stochastic algorithms with constant gains ([link](https://doi.org/10.1109/TAC.1982.1102981)) | A. Benveniste and G. Ruget | IEEE Transactions on Automatic Control |
| 34 | 2007 | 5.6 | An Analogue of Shannon Information Theory for Detection and Stabilization via Noisy Discrete Communication Channels ([link](https://doi.org/10.1137/040621697)) | A. Matveev and A. Savkin | SIAM J. Control. Optim. |
| 35 | 2010 | 5.8 | Stabilization and Disturbance Attenuation Over a Gaussian Communication Channel ([link](https://doi.org/10.1109/TAC.2010.2040507)) | J. Freudenberg, R. Middleton, and V. Solo | IEEE Transactions on Automatic Control |
| 36 | 2007 |  | Disturbance Rejection with Communication Constraints ([link](https://doi.org/10.9746/VE.SICETR1965.43.806)) | Hidenori Shingin and Y. Ohta | Journal of the Society of Instrument and Control Engineers |
| 37 | 2016 | 4.4 | The Value of Timing Information in Event-Triggered Control ([link](https://doi.org/10.1109/TAC.2019.2919107)) | M. J. Khojasteh, Pavankumar Tallapragada, J. Cortés, and M. Franceschetti | IEEE Transactions on Automatic Control |
| 38 | 2005 | 3.9 | Multirate Stabilization of Linear Multiple Sensor Systems via Limited Capacity Communication Channels ([link](https://doi.org/10.1137/S0363012902419965)) | A. Matveev and A. Savkin | SIAM J. Control. Optim. |
| 39 | 2017 |  | Control Capacity ([link](https://doi.org/10.1109/TIT.2018.2868929)) | G. Ranade and Anant Sahai | IEEE Transactions on Information Theory |
| 40 | 2007 | 2.3 | Synchronization of nonlinear systems under information constraints. ([link](https://doi.org/10.1063/1.2977459)) | Alexander L. Fradkov, B. Andrievsky, and R. Evans | Chaos |
| 41 | 1985 | 1.9 | Tracking error bounds of adaptive nonstationary filtering ([link](https://doi.org/10.1016/0005-1098(85%2990062-7)) | E. Eweda and O. Macchi | Autom. |
| 42 | 2007 | 3.5 | Feedback Stabilization Over Signal-to-Noise Ratio Constrained Channels ([link](https://doi.org/10.1109/TAC.2007.902739)) | J. Braslavsky, R. Middleton, and J. Freudenberg | IEEE Transactions on Automatic Control |
| 43 | 2018 | 1.0 | Exploiting Timing Information in Event-Triggered Stabilization of Linear Systems With Disturbances ([link](https://doi.org/10.1109/TCNS.2020.3030008)) | M. J. Khojasteh, Mojtaba Hedayatpour, J. Cortés, and M. Franceschetti | IEEE Transactions on Control of Network Systems |
| 44 | 2004 | 20 | Stochastic linear control over a communication channel ([link](https://doi.org/10.1109/TAC.2004.834430)) | S. Tatikonda, Anant Sahai, and S. Mitter | IEEE Transactions on Automatic Control |
| 45 | 2010 | 8.6 | Minimum Data Rate for Mean Square Stabilization of Discrete LTI Systems Over Lossy Channels ([link](https://doi.org/10.1109/TAC.2010.2054890)) | Keyou You and Lihua Xie | IEEE Transactions on Automatic Control |
| 46 | 1971 | 0.1 | Linear Estimation in an Unknown Quasi-Stationary Environment ([link](https://doi.org/10.1109/TSMC.1971.4308288)) | P. Monsen | IEEE Trans. Syst. Man Cybern. |
| 47 | 2003 |  | Mutual information rate and analytic constraint in linear time invariant control systems ([link](https://www.semanticscholar.org/paper/fcfed67d3512d47fcfb4d517f88ab6762b263631)) | Zhang Hui |  |
| 48 | 2001 | 8.3 | Information-theoretic approach to the study of control systems ([link](https://doi.org/10.1016/j.physa.2003.09.007)) | H. Touchette and S. Lloyd | Physica A-statistical Mechanics and Its Applications |
| 49 | 2005 |  | The Information Cost of Loop Shaping over ([link](https://www.semanticscholar.org/paper/6dbf4aa389f9b643837652cfbe4577c29fa79e1e)) | G. Channels |  |
| 50 | 2012 | 0.1 | Networked Control Systems with Unbounded Noise under Information Constraints ([link](https://www.semanticscholar.org/paper/0fe4d854f7d368253ea1dbf223ced3c82d917905)) | Andrew P. Johnston |  |
| 51 | 1980 |  | BOUNDED EFSlOR ADllpTIvE CONTROL ([link](https://www.semanticscholar.org/paper/d46739e5264b5e92d8f4b6a1a7d7217a31673679)) | K. Narendra and B. Peterson |  |
| 52 | 1980 | 0.5 | Continuous-time tracking systems incorporating Lur’e plants with single non-linearities ([link](https://doi.org/10.1080/00207728008967006)) | L. Grujic and B. Porter | International Journal of Systems Science |
| 53 | 2011 | 12 | Minimum Data Rate for Mean Square Stabilizability of Linear Systems With Markovian Packet Losses ([link](https://doi.org/10.1109/TAC.2010.2068590)) | Keyou You and Lihua Xie | IEEE Transactions on Automatic Control |
| 54 | 2006 | 1.9 | On stabilization of nonlinear systems under data rate constraints using output measurements ([link](https://doi.org/10.1002/rnc.1060)) | C. D. Persis | International Journal of Robust and Nonlinear Control |
| 55 | 2021 | 2.1 | Directed Data-Processing Inequalities for Systems with Feedback ([link](https://doi.org/10.3390/e23050533)) | M. Derpich and Jan Østergaard | Entropy |
| 56 | 2007 | 2.5 | Stabilization with disturbance attenuation over a Gaussian channel ([link](https://doi.org/10.1109/CDC.2007.4434535)) | J. Freudenberg, R. Middleton, and J. Braslavsky | 2007 46th IEEE Conference on Decision and Control |
| 57 | 2011 | 2.2 | Achievable sensitivity bounds for MIMO control systems via an information theoretic approach ([link](https://doi.org/10.1016/j.sysconle.2010.10.014)) | H. Ishii, Kunihisa Okano, and S. Hara | Syst. Control. Lett. |
| 58 | 2009 |  | 6WRFKDVWLF&RQWURORYHU)LQLWH&DSDFLW&KDQQHOV ([link](https://www.semanticscholar.org/paper/46ac552a420e2b304b159b5982717fed8b1a6f32)) | C. Charalambous, C. Kourtellaris, and Photios A. Stavrou |  |
| 59 | 2006 |  | Minimum Rate Coding for LTI Systems Over ([link](https://www.semanticscholar.org/paper/70b624401587f980e2eb23bd02c1fae54947e078)) | S. Yüksel and T. Başar |  |
| 60 | 1993 | 3.3 | Stability of recursive stochastic tracking algorithms ([link](https://doi.org/10.1109/CDC.1993.325562)) | Lei Guo | Proceedings of 32nd IEEE Conference on Decision and Control |
| 61 | 2007 | 0.2 | Data rate theorem for stabilization over fading channels ( Invited Paper ) ([link](https://www.semanticscholar.org/paper/07eb9a231edf11a175f5b034dff304166ae2b158)) | Paolo Minero, M. Franceschetti, S. Dey, and G. Nair |  |
| 62 | 2017 | 1.8 | Design constraints and limits of networked feedback in disturbance attenuation: An information-theoretic analysis ([link](https://doi.org/10.1016/j.automatica.2017.01.005)) | Song Fang, Jie Chen, and H. Ishii | Autom. |
| 63 | 2013 | 0.8 | Fundamental Inequalities and Identities Involving Mutual and Directed Informations in Closed-Loop Systems ([link](https://www.semanticscholar.org/paper/9cf0e3447c14cef2ff7e6a8ed532e1a3b554e004)) | M. Derpich, Eduardo I. Silva, and Jan Østergaard | ArXiv |
| 64 | 1991 | 0.6 | New approach to robust model reference adaptive control for a class of plants ([link](https://doi.org/10.1080/00207179108953680)) | L. Fu | International Journal of Control |
| 65 | 2018 | 1.4 | Event-triggered stabilization of disturbed linear systems over digital channels ([link](https://doi.org/10.1109/CISS.2018.8362261)) | M. J. Khojasteh, Mojtaba Hedayatpour, J. Cortés, and M. Franceschetti | 2018 52nd Annual Conference on Information Sciences and Systems (CISS) |
| 66 | 2010 | 0.4 | Control-theoretic Approach to Communication with Feedback: Fundamental Limits and Code Design ([link](https://www.semanticscholar.org/paper/404aa086bc6f249da248add53bfb420b84cd50a7)) | Ehsan Ardestanizadeh and M. Franceschetti | ArXiv |
| 67 | 2015 | 2.7 | Control capacity ([link](https://doi.org/10.1109/ISIT.2015.7282850)) | G. Ranade and Anant Sahai | 2015 IEEE International Symposium on Information Theory (ISIT) |
| 68 | 2017 | 2.0 | Tradeoffs in Networked Feedback Systems: From Information-Theoretic Measures to Bode-Type Integrals ([link](https://doi.org/10.1109/TAC.2016.2571660)) | Song Fang, H. Ishii, and Jie Chen | IEEE Transactions on Automatic Control |
| 69 | 2007 | 12 | Minimal data rate stabilization of nonlinear systems over networks with large delays ([link](https://doi.org/10.1109/WIOPT.2007.4480114)) | C. D. Persis | 2007 5th International Symposium on Modeling and Optimization in Mobile, Ad Hoc and Wireless Networks and Workshops |
| 70 | 2014 | 0.1 | Passification-based adaptive control with quantized measurements ([link](https://doi.org/10.3182/20140824-6-ZA-1003.00505)) | A. Selivanov, Alexander L. Fradkov, and D. Liberzon | IFAC Proceedings Volumes |
| 71 | 1992 | 0.7 | The error variance of LMS with time-varying weights ([link](https://doi.org/10.1109/78.127953)) | V. Solo | IEEE Trans. Signal Process. |
| 72 | 2004 | 3.1 | An analogue of Shannon information theory for networked control systems: State estimation via a noisy discrete channel ([link](https://doi.org/10.1109/CDC.2004.1429458)) | A. Matveev and A. Savkin | 2004 43rd IEEE Conference on Decision and Control (CDC) (IEEE Cat. No.04CH37601) |
| 73 | 2002 | 9.9 | Towards the Control of Linear Systems with Minimum Bit-Rate ([link](https://www.semanticscholar.org/paper/b72f6715cece3f0d4fc696236313ddac141af641)) | J. Hespanha, Antonio Ortega, and L. Vasudevan |  |
| 74 | 1997 | 1.9 | Necessary and sufficient conditions for stability of LMS ([link](https://doi.org/10.1109/9.587328)) | Lei Guo, L. Ljung, and Guanli Wang | IEEE Trans. Autom. Control. |
| 75 | 2013 | 6.8 | Stabilization of Networked Multi-Input Systems With Channel Resource Allocation ([link](https://doi.org/10.1109/TAC.2012.2218065)) | L. Qiu, G. Gu, and Wei Chen | IEEE Transactions on Automatic Control |
| 76 | 2012 |  | Stability across a Gaussian Product Channel : Necessary and Sufficient Conditions ([link](https://www.semanticscholar.org/paper/ed64cdb7939571cce3fddd5dc0915fcd829f481c)) | Utsaw Kumar, V. Gupta, and J. N. Laneman |  |
| 77 | 2007 | 0.5 | Control of Feedback Systems Subject to the Finite Rate Constraints via the Shannon Lower Bound ([link](https://doi.org/10.1109/WIOPT.2007.4480070)) | C. Charalambous and A. Farhadi | 2007 5th International Symposium on Modeling and Optimization in Mobile, Ad Hoc and Wireless Networks and Workshops |
| 78 | 2019 | 0.8 | Power Gain Bounds of MIMO Networked Control Systems: An Entropy Perspective ([link](https://doi.org/10.1109/TAC.2018.2839527)) | Song Fang, Jie Chen, and H. Ishii | IEEE Transactions on Automatic Control |
| 79 | 2008 | 0.3 | Performance Analysis of Control Systems under Limited Data Rates ([link](https://doi.org/10.9746/VE.SICETR1965.44.396)) | H. Ishii, C. Ohyama, and K. Tsumura | Journal of the Society of Instrument and Control Engineers |
| 80 | 1991 |  | Reduced-Order Adaptive Observation with Nonspecific Adaptive Law ([link](https://www.semanticscholar.org/paper/23d08f3090fc455aafc12dc28fcde5252cb2fb66)) | J. Ackermann |  |
| 81 | 2005 |  | Robust Entropy Rate for Uncertain Sources and its Applications in Controlling Systems Subject to Capacity Constraints ∗ ([link](https://www.semanticscholar.org/paper/9ba3f29f173db83e539c502260e304b77a6f0ea0)) | C. Charalambous |  |
| 82 | 1994 | 0.1 | A robust algorithm for random parameter tracking ([link](https://doi.org/10.1109/9.293180)) | A. Juditsky and P. Priouret | IEEE Trans. Autom. Control. |
| 83 | 1985 | 0.1 | An information-theoretical approach to regulation ([link](https://doi.org/10.1080/0020718508961147)) | S. Engell | International Journal of Control |
| 84 | 1979 | 2.1 | Digital adaptive filters: Conditions for convergence, rates of convergence, effects of noise and errors arising from the implementation ([link](https://doi.org/10.1109/TIT.1979.1056103)) | A. Weiss and D. Mitra | IEEE Trans. Inf. Theory |
| 85 | 1995 | 2.5 | Exponential stability of general tracking algorithms ([link](https://doi.org/10.1109/9.402229)) | Lei Guo and L. Ljung | IEEE Trans. Autom. Control. |
| 86 | 1986 | 2.0 | Parameter drift in LMS adaptive filters ([link](https://doi.org/10.1109/TASSP.1986.1164874)) | W. Sethares, D. Lawrence, C. Johnson, and R. Bitmead | IEEE Trans. Acoust. Speech Signal Process. |
| 87 | 2003 | 0.7 | Bode integrals and laws of variety in linear control systems ([link](https://doi.org/10.1109/ACC.2003.1238915)) | Hui Zhang and Youxian Sun | Proceedings of the 2003 American Control Conference, 2003. |
| 88 | 2004 | 0.5 | Regulator constrained control and rate problem for linear systems with additive disturbances ([link](https://doi.org/10.23919/ACC.2004.1384430)) | F. Mesquine, F. Tadeo, and A. Benzaouia | Proceedings of the 2004 American Control Conference |
| 89 | 2003 |  | Entropy rate and H\_∞, entropy in LTI control systems ([link](https://www.semanticscholar.org/paper/007f07dd498ce696ba2a3cc253e1e4d909a787f8)) | Sun You-xian | Control theory & applications |
| 90 | 2008 | 1.5 | Channel signal-to-noise ratio constrained feedback control: performance and robustness ([link](https://doi.org/10.1049/IET-CTA:20070246)) | A. Rojas, J. Braslavsky, and R. Middleton | Iet Control Theory and Applications |
| 91 | 2019 | 0.3 | Information-Theoretic Performance Limitations of Feedback Control: Underlying Entropic Laws and Generic $`\mathcal{L}_{p}`$ Bounds ([link](https://doi.org/10.23919/ACC50511.2021.9483083)) | Song Fang and Quanyan Zhu | 2021 American Control Conference (ACC) |
| 92 |  | 1 | Stabilization over discrete memoryless and wideband channels using nearly memoryless observations ([link](https://www.semanticscholar.org/paper/38b8e921dd5aa6c946b4e3eea0b2a84ef6724a34)) | Anant Sahai |  |
| 93 | 2018 | 0.5 | Non-asymptotic error bounds for constant stepsize stochastic approximation for tracking mobile agents ([link](https://doi.org/10.1007/s00498-019-00249-4)) | Bhumesh Kumar, V. Borkar, and A. Shetty | Mathematics of Control, Signals, and Systems |
| 94 | 2016 | 3.2 | Causality preserving information transfer measure for control dynamical system ([link](https://doi.org/10.1109/CDC.2016.7799401)) | S. Sinha and U. Vaidya | 2016 IEEE 55th Conference on Decision and Control (CDC) |
| 95 | 2009 |  | An Analog of Shannon Information Theory: State Estimation and Stabilization of Linear Noisy Plants via Noisy Discrete Channels ([link](https://doi.org/10.1007/978-0-8176-4607-3_7)) | A. Matveev and A. Savkin |  |
| 96 | 2019 | 3.5 | Fundamental limitations and intrinsic limits of feedback: An overview in an information age ([link](https://doi.org/10.1016/J.ARCONTROL.2019.03.011)) | Jie Chen, Song Fang, and H. Ishii | Annu. Rev. Control. |
| 97 | 2021 | 1.1 | Sensitivity minimization, biological homeostasis and information theory ([link](https://doi.org/10.1007/s00422-021-00860-2)) | Debojyoti Biswas and P. Iglesias | Biological Cybernetics |
| 98 | 2003 | 0.4 | Information theoretic limit and bound of disturbance rejection in LTI systems: Shannon entropy and H/sub /spl infin// entropy ([link](https://doi.org/10.1109/ICSMC.2003.1244604)) | Hui Zhang and Youxian Sun | SMC’03 Conference Proceedings. 2003 IEEE International Conference on Systems, Man and Cybernetics. Conference Theme - System Security and Assurance (Cat. No.03CH37483) |
| 99 | 2019 | 1.2 | Sensitivity analysis of linear continuous-time feedback systems subject to control and measurement noise: An information-theoretic approach ([link](https://doi.org/10.1016/j.sysconle.2019.104548)) | Neng Wan, Dapeng Li, and N. Hovakimyan | Syst. Control. Lett. |
| 100 | 2020 | 0.5 | Tracking Performance of Online Stochastic Learners ([link](https://doi.org/10.1109/LSP.2020.3013775)) | Stefan Vlaski, Elsa Rizk, and A. H. Sayed | IEEE Signal Processing Letters |
| 101 | 1997 | 0.3 | Comparison of tracking algorithms for single layer threshold networks in the presence of random drift ([link](https://doi.org/10.1109/78.558480)) | A. Kuh | IEEE Trans. Signal Process. |
| 102 | 2010 | 30 | Fundamental limits on the suppression of molecular fluctuations ([link](https://doi.org/10.1038/nature09333)) | Ioannis Lestas, G. Vinnicombe, and J. Paulsson | Nature |
| 103 | 2002 | 12 | Limited Data Rate in Control Systems with Networks ([link](https://doi.org/10.1007/3-540-45796-8)) | H. Ishii and B. Francis |  |

### Paper Details

1\. · 100% match · 2004 · 80 cit/yr\
**Control under communication constraints** ([link](https://doi.org/10.1109/TAC.2004.831187))\
S. Tatikonda and S. Mitter\
*IEEE Transactions on Automatic Control* · Jul 12, 2004 · 1745 citations

------------------------------------------------------------------------

2\. · 100% match · 2006 · 21 cit/yr\
**The Necessity and Sufficiency of Anytime Capacity for Stabilization of a Linear System Over a Noisy Communication Link—Part I: Scalar Systems** ([link](https://doi.org/10.1109/TIT.2006.878169))\
Anant Sahai and S. Mitter\
*IEEE Transactions on Information Theory* · Jan 4, 2006 · 432 citations

> In this paper, we review how Shannon’s classical notion of capacity is not enough to characterize a noisy communication channel if the channel is intended to be used as part of a feedback loop to stabilize an unstable scalar linear system. While classical capacity is not enough, another sense of capacity (parametrized by reliability) called “anytime capacity” is necessary for the stabilization of an unstable process. The required rate is given by the log of the unstable system gain and the required reliability comes from the sense of stability desired. A consequence of this necessity result is a sequential generalization of the Schalkwijk-Kailath scheme for communication over the additive white Gaussian noise (AWGN) channel with feedback. In cases of sufficiently rich information patterns between the encoder and decoder, adequate anytime capacity is also shown to be sufficient for there to exist a stabilizing controller. These sufficiency results are then generalized to cases with noisy observations, delayed control actions, and without any explicit feedback between the observer and the controller. Both necessary and sufficient conditions are extended to continuous time systems as well. We close with comments discussing a hierarchy of difficulty for communication problems and how these results establish where stabilization problems sit in that hierarchy

------------------------------------------------------------------------

3\. · 100% match · 2004 · 34 cit/yr\
**Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates** ([link](https://doi.org/10.1137/S0363012902402116))\
G. Nair and R. Evans\
*SIAM J. Control. Optim.* · Feb 1, 2004 · 753 citations

> Feedback control with limited data rates is an emerging area which incorporates ideas from both control and information theory. A fundamental question it poses is how low the closed-loop data rate can be made before a given dynamical system is impossible to stabilize by any coding and control law. Analogously to source coding, this defines the smallest error-free data rate sufficient to achieve “reliable” control, and explicit expressions for it have been derived for linear time-invariant systems without disturbances. In this paper, the more general case of finite-dimensional linear systems with process and observation noise is considered, the object being mean square state stability. By inductive arguments employing the entropy power inequality of information theory, and a new quantizer error bound, an explicit expression for the infimum stabilizing data rate is derived, under very mild conditions on the initial state and noise probability distributions.

------------------------------------------------------------------------

4\. · 100% match · 1999 · 34 cit/yr\
**Systems with finite communication bandwidth constraints. II. Stabilization with limited information feedback** ([link](https://doi.org/10.1109/9.763226))\
W. Wong and R. Brockett\
*IEEE Trans. Autom. Control.* · May 1, 1999 · 930 citations

> For part I, see ibid., vol.42, p.1294-8, 1997. In this paper a new class of feedback control problems is introduced. Unlike classical models, the systems considered here have communication channel constraints. As a result, the issue of coding and communication protocol becomes an integral part of the analysis. Since these systems cannot be asymptotically stabilized if the underlying dynamics are unstable, a weaker stability concept called containability is introduced. A key result connects containability with an inequality equation involving the communication data rate and the rate of change of the state.

------------------------------------------------------------------------

5\. · 100% match · 2009 · 13 cit/yr\
**Data Rate Theorem for Stabilization Over Time-Varying Feedback Channels** ([link](https://doi.org/10.1109/TAC.2008.2010887))\
Paolo Minero, M. Franceschetti, S. Dey, and G. Nair\
*IEEE Transactions on Automatic Control* · Feb 10, 2009 · 224 citations

------------------------------------------------------------------------

6\. · 100% match · 2012 · 2.6 cit/yr\
**Characterization of Information Channels for Asymptotic Mean Stationarity and Stochastic Stability of Nonstationary/Unstable Linear Systems** ([link](https://doi.org/10.1109/TIT.2012.2204033))\
S. Yüksel\
*IEEE Transactions on Information Theory* · Jan 25, 2012 · 37 citations

> Stabilization of nonstationary linear systems over noisy communication channels is considered. Stochastically stable sources, and unstable but noise-free or bounded-noise systems have been extensively studied in the information theory and control theory literature since the 1970s, with a renewed interest in the past decade. There have also been studies on noncausal and causal coding of unstable/nonstationary linear Gaussian sources. In this paper, tight necessary and sufficient conditions for stochastic stabilizability of unstable (nonstationary) possibly multidimensional linear systems driven by Gaussian noise over discrete channels (possibly with memory and feedback) are presented. Stochastic stability notions include recurrence, asymptotic mean stationarity and sample path ergodicity, and the existence of finite second moments. Our constructive proof uses random-time state-dependent stochastic drift criteria for stabilization of Markov chains. For asymptotic mean stationarity (and thus sample path ergodicity), it is sufficient that the capacity of a channel is (strictly) greater than the sum of the logarithms of the unstable pole magnitudes for memoryless channels and a class of channels with memory. This condition is also necessary under a mild technical condition. Sufficient conditions for the existence of finite average second moments for such systems driven by unbounded noise are provided.

------------------------------------------------------------------------

7\. · 100% match · 1966 · 10 cit/yr\
**On the input-output stability of time-varying nonlinear feedback systems–Part II: Conditions involving circles in the frequency plane and sector nonlinearities** ([link](https://doi.org/10.1109/TAC.1966.1098356))\
G. Zames\
*IEEE Transactions on Automatic Control* · Jul 1, 1966 · 625 citations

> The object of this paper is to outline a stability theory based on functional methods. Part I of the paper was devoted to a general feedback configuration. Part II is devoted to a feedback system consisting of two elements, one of which is linear time-invariant, and the other nonlinear. An attempt is made to unify several stability conditions, including Popov’s condition, into a single principle. This principle is based on the concepts of conicity and positivity, and provides a link with the notions of gain and phase shift of the linear theory. Part II draws on the (generalized) notion of a “sector non-linearity.” A nonlinearity N is said to be INSIDE THE SECTOR {\alpha,\beta} if it satisfies an inequality of the type \langle(Nx-\alphax)*{t}, (Nx-\betax)*{t}\rangle\leq0 . If N is memoryless and is characterized by a graph in the plane, then this simply means that the graph lies inside a sector of the plane. However, the preceding definition extends the concept to include nonlinearities with memory. There are two main results. The first result, the CIRCLE THEOREM, asserts in part that: If the nonlinearity is inside a sector {\alpha, \beta} , and if the frequency response of the linear element avoids a “critical region” in the complex plane, then the closed loop is bounded; if \alpha \> 0 then the critical region is a disk whose center is halfway between the points -1/\alpha and -1/\beta , and whose diameter is greater than the distance between these points. The second result is a method for taking into account the detailed properties of the nonlinearity to get improved stability conditions. This method involves the removal of a “multiplier” from the linear element. The frequency response of the linear element is modified by the removal, and, in effect, the size of the critical region is reduced. Several conditions, including Popov’s condition, are derived by this method, under various restrictions on the nonlinearity N ; the following cases are treated: (i) N is instantaneously inside a sector {\alpha, \beta} . (ii) N satisfies (i) and is memoryless and time-invariant. (iii) N satisfies (ii) and has a restricted slope.

------------------------------------------------------------------------

8\. · 100% match · 2008 · 15 cit/yr\
**Feedback Control in the Presence of Noisy Channels: “Bode-Like” Fundamental Limitations of Performance** ([link](https://doi.org/10.1109/TAC.2008.929361))\
N. C. Martins and M. Dahleh\
*IEEE Transactions on Automatic Control* · Sep 9, 2008 · 273 citations

------------------------------------------------------------------------

9\. · 100% match · 2000 · 65 cit/yr\
**Quantized feedback stabilization of linear systems** ([link](https://doi.org/10.1109/9.867021))\
R. Brockett and D. Liberzon\
*IEEE Trans. Autom. Control.* · Jul 1, 2000 · 1678 citations

> This paper addresses feedback stabilization problems for linear time-invariant control systems with saturating quantized measurements. We propose a new control design methodology, which relies on the possibility of changing the sensitivity of the quantizer while the system evolves. The equation that describes the evolution of the sensitivity with time (discrete rather than continuous in most cases) is interconnected with the given system (either continuous or discrete), resulting in a hybrid system. When applied to systems that are stabilizable by linear time-invariant feedback, this approach yields global asymptotic stability.

------------------------------------------------------------------------

10\. · 100% match · 2001 · 74 cit/yr\
**Stabilization of linear systems with limited information** ([link](https://doi.org/10.1109/9.948466))\
N. Elia and S. Mitter\
*IEEE Trans. Autom. Control.* · Sep 1, 2001 · 1817 citations

> We show that the coarsest, or least dense, quantizer that quadratically stabilizes a single input linear discrete time invariant system is logarithmic, and can be computed by solving a special linear quadratic regulator problem. We provide a closed form for the optimal logarithmic base exclusively in terms of the unstable eigenvalues of the system. We show how to design quantized state-feedback controllers, and quantized state estimators. This leads to the design of hybrid output feedback controllers. The theory is then extended to sampling and quantization of continuous time linear systems sampled at constant time intervals. We generalize the definition of density of quantization to the density of sampling and quantization in a natural way, and search for the coarsest sampling and quantization scheme that ensures stability. Finally, by relaxing the definition of quadratic stability, we show how to construct logarithmic quantizers with only finite number of quantization levels and still achieve practical stability of the closed-loop system.

------------------------------------------------------------------------

11\. · 100% match · 2000 · 13 cit/yr\
**Stabilization with data-rate-limited feedback: tightest attainable bounds** ([link](https://doi.org/10.1016/S0167-6911(00%2900037-2))\
G. Nair and R. Evans\
*Systems & Control Letters* · Sep 15, 2000 · 327 citations

------------------------------------------------------------------------

12\. · 100% match · 1984 · 4.2 cit/yr\
**On the statistical efficiency of the LMS algorithm with nonstationary inputs** ([link](https://doi.org/10.1109/TIT.1984.1056892))\
B. Widrow and E. Walach\
*IEEE Trans. Inf. Theory* · May 22, 1984 · 177 citations

> A fundamental relationship exists between the quality of an adaptive solution and the amount of data used in obtaining it. Quality is defined here in terms of “misadjustment,” the ratio of the excess mean square error (mse) in an adaptive solution to the minimum possible mse. The higher the misadjustment, the lower the quality is. The quality of the exact least squares solution is compared with the quality of the solutions obtained by the orthogonalized and the conventional least mean square (LMS) algorithms with stationary and nonstationary input data. When adapting with noisy observations, a filter trained with a finite data sample using an exact least squares algorithms will have a misadjustment given by M=\frac{n}{N}=\frac{number of weights}{number of training samples} If the same adaptive filter were trained with a steady flow of data using an ideal “orthogonalized LMS” algorithm, the misadjustment would be M=\frac{n}{4\tau\_{\mse}}=\frac{number of weights}{number of training samples} Thus, for a given time constant \tau\_{\mse} of the learning process, the ideal orthogonalized LMS algorithm will have about as low a misadjustment as can be achieved, since this algorithm performs essentially as an exact least squares algorithm with exponential data weighting. It is well known that when rapid convergence with stationary data is required, exact least squares algorithms can in certain cases outperform the conventional Widrow-Hoff LMS algorithm. It is shown here, however, that for an important class of nonstationary problems, the misadjustment of conventional LMS is the same as that of orthogonalized LMS, which in the stationary case is shown to perform essentially as an exact least squares algorithm.

------------------------------------------------------------------------

13\. · 100% match · 2006 · 1.7 cit/yr\
**The necessity and sufficiency of anytime capacity for stabilization of a linear system over a noisy communication link, Part II: vector systems** ([link](https://www.semanticscholar.org/paper/30bacce26f417f7ae9dde9ce6196870496f30f12))\
Anant Sahai and S. Mitter\
*arXiv: Information Theory* · Jan 4, 2006 · 34 citations

> In part I, we reviewed how Shannon’s classical notion of capacity is not sufficient to characterize a noisy communication channel if the channel is intended to be used as part of a feedback loop to stabilize an unstable scalar linear system. While classical capacity is not enough, a sense of capacity (parametrized by reliability) called “anytime capacity” is both necessary and sufficient for channel evaluation in this context. The rate required is the log of the open-loop system gain and the required reliability comes from the desired sense of stability. Sufficiency is maintained even in cases with noisy observations and without any explicit feedback between the observer and the controller. This established the asymptotic equivalence between scalar stabilization problems and delay-universal communication problems with feedback. Here in part II, the vector-state generalizations are established and it is the magnitudes of the unstable eigenvalues that play an essential role. To deal with such systems, the concept of the anytime rate-region is introduced. This is the region of rates that the channel can support while still meeting potentially different anytime reliability targets for parallel message streams. All the scalar results generalize on an eigenvalue by eigenvalue basis. When there is no explicit feedback of the noisy channel outputs, the intrinsic delay of the unstable system tells us what the feedback delay needs to be while evaluating the anytime-rate-region for the channel. An example involving a binary erasure channel is used to illustrate how differentiated service is required in any separation-based control architecture.

------------------------------------------------------------------------

14\. · 100% match · 2015 · 3.9 cit/yr\
**Input-to-state stability of Lur’e systems** ([link](https://doi.org/10.1007/S00498-015-0147-0))\
E. Sarkans and H. Logemann\
*Mathematics of Control, Signals, and Systems* · Jul 18, 2015 · 42 citations

> An input-to-state stability theory, which subsumes results of circle criterion type, is developed in the context of continuous-time Lur’e systems. The approach developed is inspired by the complexified Aizerman conjecture.

------------------------------------------------------------------------

15\. · 100% match · 2004 · 18 cit/yr\
**When bode meets shannon: control-oriented feedback communication schemes** ([link](https://doi.org/10.1109/TAC.2004.834119))\
N. Elia\
*IEEE Transactions on Automatic Control* · Sep 13, 2004 · 391 citations

------------------------------------------------------------------------

16\. · 100% match · 1976 · 29 cit/yr\
**Stationary and nonstationary learning characteristics of the LMS adaptive filter** ([link](https://doi.org/10.1007/978-94-010-1223-2_23))\
B. Widrow, J. Mccool, M. Larimore, and C. Johnson\
*Proceedings of the IEEE* · Aug 1, 1976 · 1464 citations

------------------------------------------------------------------------

17\. · 100% match · 2015 · 3.4 cit/yr\
**Passification based synchronization of nonlinear systems under communication constraints and bounded disturbances** ([link](https://doi.org/10.1016/j.automatica.2015.03.012))\
Alexander L. Fradkov, B. Andrievsky, and M. Ananyevskiy\
*Autom.* · May 1, 2015 · 38 citations

> In brief the synchronization problem for nonlinear systems under communication constraints and bounded exogenous disturbances is analyzed. The main contribution is in the evaluation of the synchronization error as a function of transmission rate and the upper bounds of the disturbances. Relevance of passifiability condition for controlled synchronization of master-slave nonlinear systems for first order coder/decoder pair is demonstrated. Experimental results obtained at three-computer setup, illustrating the theory are presented.

------------------------------------------------------------------------

18\. · 100% match · 2003 · 7.9 cit/yr\
**On stabilization of linear systems with limited information** ([link](https://doi.org/10.1109/TAC.2002.808487))\
D. Liberzon\
*IEEE Trans. Autom. Control.* · Apr 1, 2003 · 183 citations

> We consider the problem of stabilizing a linear time-invariant system using sampled encoded measurements of its state or output. We derive a relationship between the number of values taken by the encoder and the norm of the transition matrix of the open-loop system over one sampling period, which guarantees that global asymptotic stabilization can be achieved. A coding scheme and a stabilizing control strategy are described explicitly.

------------------------------------------------------------------------

19\. · 100% match · 2014 · 4.6 cit/yr\
**A Characterization of the Minimal Average Data Rate That Guarantees a Given Closed-Loop Performance Level** ([link](https://doi.org/10.1109/TAC.2015.2500658))\
Eduardo I. Silva, M. Derpich, Jan Østergaard, and Marco A. Encina\
*IEEE Transactions on Automatic Control* · Jul 1, 2014 · 55 citations

> This paper studies networked control systems closed over noiseless digital channels. We focus on noisy linear time-invariant (LTI) plants with stationary Gaussian disturbances, Gaussian initial state, scalar-valued control inputs and sensor outputs. For this set-up, we show that the absolute minimal directed information rate that allows one to achieve a prescribed level of performance (not necessarily stationary), over all combinations of encoder-controller-decoder, is achieved when the decoder output is jointly Gaussian with the other signals in the system. This directed information rate lower bounds the achievable operational data rates. When restricting our attention to encoder-controller-decoders which make the random processes in the loop (strongly) asymptotically wide-sense stationary, this bound can be expressed in terms of their asymptotic power spectral densities. Then we show that the directed information rate and stationary performance of any such scheme can be achieved when the concatenated encoder, channel, controller and decoder behave as an AWGN channel with LTI filters. We also present a simple coding scheme that allows one to achieve (operational) average data rates that are at most (approximately) 1.254 bits away from the derived lower bound, while satisfying the performance constraint. A numerical example is presented to illustrate our findings.

------------------------------------------------------------------------

20\. · 100% match · 2009 · 1.9 cit/yr\
**Disturbance rejection with information constraints: Performance limitations of a scalar system for bounded and Gaussian disturbances** ([link](https://doi.org/10.1016/j.automatica.2012.02.040))\
Hidenori Shingin and Y. Ohta\
*Autom.* · Sep 1, 2009 · 32 citations

------------------------------------------------------------------------

21\. · 100% match · 2007 · 3.6 cit/yr\
**Shannon zero error capacity in the problems of state estimation and stabilization via noisy communication channels** ([link](https://doi.org/10.1080/002071706000981775))\
A. Matveev and A. Savkin\
*Int. J. Control* · Feb 20, 2007 · 69 citations

> The paper addresses state estimation and stabilization problems involving communication errors and capacity constraints. Discrete-time partially observed unstable linear systems perturbed by stochastic exogenous disturbances are studied. Unlike the classic theory, the sensor signals are transmitted to the estimator or controller over a noisy digital communication link modelled as a stochastic stationary discrete memoryless channel. It is shown that the capability of the noisy channel to ensure almost sure stabilizability/observability of the plant is identical to exactly its capability to transmit information with zero probability of error. Specifically, it is demonstrated that the standard numerical characteristic of the latter capability, i.e., the Shannon zero error capacity of the channel, constitutes the border separating the cases where the plant is and respectively, is not stabilizable/observable with probability 1.

------------------------------------------------------------------------

22\. · 100% match · 1987 · 1.7 cit/yr\
**Nonstationary learning characteristics of the LMS algorithm** ([link](https://doi.org/10.1109/TCS.1987.1086054))\
W. Gardner\
Oct 1, 1987 · 67 citations

> Upper and lower bounding first-order linear recursions for the mean-squared error realized with the LMS algorithm subjected to a sequence of independent nonstationary training vectors are derived. These bounds coincide to give the exact evolution of mean-squared error for the problem of identification of a nonrecursive time-varying system with white-noise excitation. This leads to an exact formula for time-averaged mean-squared error that is used to study optimization of the step-size parameter for minimum time-average misadjustment. New results on dependence of the minimal step size and the minimum misadjustment on the degree of nonstationarity are obtained.

------------------------------------------------------------------------

23\. · 100% match · 2015 · 2.1 cit/yr\
**Stationary and Ergodic Properties of Stochastic NonLinear Systems Controlled over Communication Channels** ([link](https://doi.org/10.1137/140989686))\
S. Yüksel\
*SIAM J. Control. Optim.* · Jun 12, 2015 · 23 citations

> This paper is concerned with the following problem: Given a stochastic non-linear system controlled over a noisy channel, what is the largest class of channels for which there exist coding and control policies so that the closed loop system is stochastically stable? Stochastic stability notions considered are stationarity, ergodicity or asymptotic mean stationarity. We do not restrict the state space to be compact, for example systems considered can be driven by unbounded noise. Necessary and sufficient conditions are obtained for a large class of systems and channels. A generalization of Bode’s Integral Formula for a large class of non-linear systems and information channels is obtained. The findings generalize existing results for linear systems.

------------------------------------------------------------------------

24\. · 100% match · 1988 · 0.2 cit/yr\
**Algebraic conditions for absolute tracking control of Lurie systems** ([link](https://doi.org/10.1080/00207178808906207))\
L. Grujic\
*International Journal of Control* · Aug 1, 1988 · 6 citations

> By definition, the goal of control is to force the system’s real output to track its desired output despite actions of external disturbances. Both continuous-time and discrete-time Lurie systems with time-varying desired outputs are considered, subject to time-varying unknown unmeasurable disturbances. The absolute tracking concept is introduced in this framework via the state-space and various tracking properties are discovered and denned. These properties reflect different qualities of the system’s dynamic behaviour. New qualitative and conceptual necessary conditions are established for all tracking properties. These uncover the crucial necessary relationships between the sets of admissible desired outputs, acceptable disturbances and realizable controls. General sufficient conditions are derived so that system tracking in a ‘forced regime’ is guaranteed by the adequate stability of an appropriately associated system in the ‘free regime’. The general sufficient conditions are basic for the application …

------------------------------------------------------------------------

25\. · 100% match · 2011 · 4.1 cit/yr\
**A Framework for Control System Design Subject to Average Data-Rate Constraints** ([link](https://doi.org/10.1109/TAC.2010.2098070))\
Eduardo I. Silva, M. Derpich, and Jan Østergaard\
*IEEE Transactions on Automatic Control* · Aug 1, 2011 · 61 citations

------------------------------------------------------------------------

26\. · 100% match · 1991 · 1.1 cit/yr\
**A result on the mean square error obtained using general tracking algorithms** ([link](https://doi.org/10.1002/ACS.4480050402))\
L. Ljung and P. Priouret\
*International Journal of Adaptive Control and Signal Processing* · Jul 1, 1991 · 37 citations

> Tracking time-varying properties is of crucial importance in all adaptive algorithms. In this contribution we study a fairly general algorithm for tracking properties of model parameters that can be described in a linear regression form (including AR models and the like). An explicit expression for the mean square error between the estimated and the true (time-varying) parameter is established. For slow adaptation this expression can be arbitrarily well approximated by a much simpler expression. The treatment differs from other related studies using weak convergence theory, averaging, etc. in that the results are not asymptotic in nature and are applicable also to the transient phase as well as over unbounded time intervals.

------------------------------------------------------------------------

27\. · 100% match · 1969 · 0.6 cit/yr\
**The Information Transfer Required in Regulatory Processes** ([link](https://doi.org/10.1109/TSSC.1969.300226))\
R. Conant\
*IEEE Trans. Syst. Sci. Cybern.* · Oct 1, 1969 · 35 citations

> Several fundamental relations between regulation and informational quantities are given. These show that regulation is a phenomenon closely tied to the transinformation between the regulator and the system which might be called its opponent. Two basic types of regulators are distinguished. The first, error-controlled regulators, are shown to be essentially coding devices which operate by taking advantage of constraints in the input sequence. The second, cause-controlled regulators, are shown to be free of some limitations inherent in error-controlled regulators. The importance of the regulator’s channel capacity in cause-controlled regulation is established.

------------------------------------------------------------------------

28\. · 100% match · 1980 · 1.4 cit/yr\
**Tracking properties of adaptive signal processing algorithms** ([link](https://doi.org/10.1109/ICASSP.1980.1170938))\
D. Farden and K. Sayood\
*IEEE International Conference on Acoustics, Speech, and Signal Processing* · Apr 9, 1980 · 63 citations

> Adaptive signal processing algorithms are often used in order to “track” an unknown time-varying parameter vector. Such algorithms are typically some form of stochastic gradient-descent algorithm. The Widrow LMS algorithm is apparently the most frequently used. This work develops an upper bound on the norm-squared error between the parameter vector being tracked and the value obtained by the algorithm. The upper bound illustrates the relationship between the algorithm step-size and the maximum rate of variation in the parameter vector. Finally, some simple covariance decay-rate conditions are imposed to obtain a bound on the mean square error.

------------------------------------------------------------------------

29\. · 100% match · 2009 · 1.6 cit/yr\
**Synchronization of Passifiable Lurie Systems Via Limited-Capacity Communication Channel** ([link](https://doi.org/10.1109/TCSI.2008.2001365))\
Alexander L. Fradkov, B. Andrievsky, and R. Evans\
*IEEE Transactions on Circuits and Systems I: Regular Papers* · Feb 1, 2009 · 27 citations

> Output-feedback controlled synchronization problems for a class of nonlinear unstable systems under information constraints imposed by limited capacity of the communication channel are analyzed. A binary time-varying coder-decoder scheme is described, and a theoretical analysis for multidimensional master-slave systems represented in Lurie form (linear part plus nonlinearity depending only on measurable outputs) is provided. An output-feedback control law is proposed based on the passification theorem. It is shown that the synchronization error exponentially tends to zero for sufficiently high transmission rate (channel capacity). The results obtained for the synchronization problem can be extended to tracking problems in a straightforward manner if the reference signal is described by an external (exogenous) state space model. The results are illustrated by the controlled synchronization of two chaotic Chua systems via a communication channel with limited capacity.

------------------------------------------------------------------------

30\. · 100% match · 2012 · 4.7 cit/yr\
**Minimal Bit Rates and Entropy for Exponential Stabilization** ([link](https://doi.org/10.1137/110829271))\
F. Colonius\
*SIAM J. Control. Optim.* · Oct 2, 2012 · 64 citations

> Minimal bit rates and entropy are studied for exponential stabilization of control systems in continuous time. Upper and lower bounds for the stabilization entropy are derived. In particular, for linear systems, a formula is given in terms of the real parts of eigenvalues. Then the minimal bit rate is related to the stabilization entropy.

------------------------------------------------------------------------

31\. · 100% match · 2015 · 1.1 cit/yr\
**LQG Control with Minimal Information: Three-Stage Separation Principle and SDP-based Solution Synthesis** ([link](https://www.semanticscholar.org/paper/daeb13fee5360fff8440d2a3bfc080611c1220dc))\
Takashi Tanaka, Peyman Mohajerin Esfahani, and S. Mitter\
*ArXiv* · Oct 14, 2015 · 12 citations

> In the interest of evaluating an information-theoretic requirement for feedback control, this paper proposes a framework to synthesize a control policy that minimizes Massey’s directed information from the state sequence to the control sequence while attaining required Linear-Quadratic-Gaussian (LQG) control performance. Interpretation and significance of this framework is discussed in the context of networked control theory. As the main result, we show that an optimal control policy can be realized by an attractively simple three-stage decision architecture comprising (1) a linear sensor with additive Gaussian noise, (2) a Kalman filter, and (3) a certainty equivalence controller. This result suggests an integration of two separation principles previously known in the literature: the filter-controller separation principle in the LQG control theory, and the sensorfilter separation principle in zero-delay rate-distortion theory for Gauss-Markov sources. It is also shown that an optimal policy can be synthesized by semidefinite programming (SDP). Both time-varying finite-horizon problems and time-invariant infinitehorizon problems are considered. Our results can be viewed as a generalization of the data-rate theorem for mean-square stability by Nair & Evans, extended for a control performance analysis.

------------------------------------------------------------------------

32\. · 100% match · 2018 · 3.9 cit/yr\
**Entropy and Minimal Bit Rates for State Estimation and Model Detection** ([link](https://doi.org/10.1109/TAC.2017.2782478))\
D. Liberzon and S. Mitra\
*IEEE Transactions on Automatic Control* · Oct 1, 2018 · 30 citations

> We study a notion of estimation entropy for continuous-time nonlinear systems, formulated in terms of the number of system trajectories that approximate all other trajectories up to an exponentially decaying error. We also consider an alternative definition of estimation entropy, which uses approximating functions that are not necessarily trajectories of the system, and show that the two entropy notions are equivalent. We establish an upper bound on the estimation entropy in terms of the sum of the desired convergence rate and an upper bound on the matrix measure of the Jacobian, multiplied by the system dimension. A lower bound on the estimation entropy is developed as well. We then turn our attention to state estimation and model detection with quantized and sampled state measurements. We describe an iterative procedure that uses such measurements to generate state estimates that converge to the true state at the desired exponential rate. The average bit rate utilized by this procedure matches the derived upper bound on the estimation entropy, and no other algorithm of this type can perform the same estimation task with bit rates lower than the estimation entropy. Finally, we discuss an application of the estimation procedure in determining, from the quantized state measurements, which of two competing models of a dynamical system is the true model. We show that under a mild assumption of “exponential separation” of the candidate models, detection always happens in finite time.

------------------------------------------------------------------------

33\. · 100% match · 1982 · 2.5 cit/yr\
**A measure of the tracking capability of recursive stochastic algorithms with constant gains** ([link](https://doi.org/10.1109/TAC.1982.1102981))\
A. Benveniste and G. Ruget\
*IEEE Transactions on Automatic Control* · Jun 1, 1982 · 112 citations

> A criterion is given for measuring the tracking capability of recursive algorithms when applied to slowly time-varying systems; the optimal gain for a given disturbance is also calculated. This criterion is seen to have some connection with the Fisher information matrix, and allows us to select a priori the best algorithm for identifying a given unknown parameter which may be subject to smooth unknown disturbances. Examples of applications are given in the areas of identification theory and data communication theory.

------------------------------------------------------------------------

34\. · 100% match · 2007 · 5.6 cit/yr\
**An Analogue of Shannon Information Theory for Detection and Stabilization via Noisy Discrete Communication Channels** ([link](https://doi.org/10.1137/040621697))\
A. Matveev and A. Savkin\
*SIAM J. Control. Optim.* · Sep 1, 2007 · 105 citations

> The paper addresses both detection and stabilization problems involving communication errors and capacity constraints. Discrete-time partially observed linear systems are studied. Unlike the classic theory, the sensor signals are transmitted to the estimator/controller over a noisy digital communication link modeled as a stochastic stationary discrete memoryless channel. It is shown that for noise-free plants, the Shannon capacity of the channel constitutes the border separating the cases where stabilization and reliable detection (asymptotic state estimation) with arbitrarily large probability are and are not possible, respectively.

------------------------------------------------------------------------

35\. · 100% match · 2010 · 5.8 cit/yr\
**Stabilization and Disturbance Attenuation Over a Gaussian Communication Channel** ([link](https://doi.org/10.1109/TAC.2010.2040507))\
J. Freudenberg, R. Middleton, and V. Solo\
*IEEE Transactions on Automatic Control* · Feb 5, 2010 · 95 citations

------------------------------------------------------------------------

36\. · 100% match · 2007\
**Disturbance Rejection with Communication Constraints** ([link](https://doi.org/10.9746/VE.SICETR1965.43.806))\
Hidenori Shingin and Y. Ohta\
*Journal of the Society of Instrument and Control Engineers* · Sep 30, 2007 · 0 citations

> Disturbance rejection problem with communication constraints for the first order system is considered. The performance limitation of the control system is shown by describing the trade-off between channel capacity and control performance quantitatively. The optimal control performance can be achieved by the state observation based on the coding of state prediction error and control to cancel the state by the predicted value.

------------------------------------------------------------------------

37\. · 100% match · 2016 · 4.4 cit/yr\
**The Value of Timing Information in Event-Triggered Control** ([link](https://doi.org/10.1109/TAC.2019.2919107))\
M. J. Khojasteh, Pavankumar Tallapragada, J. Cortés, and M. Franceschetti\
*IEEE Transactions on Automatic Control* · Sep 30, 2016 · 42 citations

> We study event-triggered control for stabilization of unstable linear plants over rate-limited communication channels subject to unknown bounded delay. On one hand, the timing of event triggering carries implicit information about the state of the plant. On the other hand, the delay in the communication channel causes information loss, as it makes the state information available at the controller out of date. Combining these two effects, we show a phase transition behavior in the transmission rate required for stabilization using a given event-triggering strategy. For small values of the delay, the timing information carried by the triggering events is substantial, and the system can be stabilized with any positive rate. When the delay exceeds a critical threshold, the timing information alone is not enough to achieve stabilization, and the required rate grows. When the delay equals the inverse of the entropy rate of the plant, the implicit information carried by the triggering events perfectly compensates the loss of information due to the communication delay, and we recover the rate requirement prescribed by the data-rate theorem. We also provide an explicit construction yielding a sufficient rate for stabilization, as well as results for vector systems. Our results do not rely on any a priori probabilistic model for the delay or the initial conditions.

------------------------------------------------------------------------

38\. · 100% match · 2005 · 3.9 cit/yr\
**Multirate Stabilization of Linear Multiple Sensor Systems via Limited Capacity Communication Channels** ([link](https://doi.org/10.1137/S0363012902419965))\
A. Matveev and A. Savkin\
*SIAM J. Control. Optim.* · Aug 1, 2005 · 82 citations

> The paper addresses a feedback stabilization problem involving bit-rate communication capacity constraints. A discrete-time partially observed linear system is studied. Unlike classic theory, the signals from multiple sensors are transmitted to the controller over separate finite capacity communication channels. The sensors do not have constant access to the channels, and the channels are not perfect: the messages incur time-varying transmission delays and may be corrupted or lost. However, we suppose that the time-average number of bits per sample period that can be successfully transmitted over the channel during a time interval converges to a certain limit as the length of the interval becomes large. Necessary and sufficient conditions for stabilizability are established. They give the tightest lower bounds on the channel capacities for which stabilization is possible. An algorithm for stabilization is also presented.

------------------------------------------------------------------------

39\. · 100% match · 2017\
**Control Capacity** ([link](https://doi.org/10.1109/TIT.2018.2868929))\
G. Ranade and Anant Sahai\
*IEEE Transactions on Information Theory* · Jan 16, 2017 · 0 citations

> Feedback control actively dissipates uncertainty from a dynamical system by means of actuation. We develop a notion of “control capacity” that gives a fundamental limit (in bits) on the rate at which a controller can dissipate the uncertainty from a system, i.e., stabilize to a known fixed point. We give a computable single-letter characterization of control capacity for memoryless stationary scalar multiplicative actuation channels. Control capacity allows us to answer questions of stabilizability for scalar linear systems: a system with actuation uncertainty is stabilizable if and only if the control capacity is larger than the log of the unstable open-loop eigenvalue. For second-moment senses of stability, we recover the classic uncertainty threshold principle result. However, our definition of control capacity can quantify the stabilizability limits for any moment of stability. Our formulation parallels the notion of Shannon’s communication capacity and thus yields both a strong converse and a way to compute the value of side information in control.

------------------------------------------------------------------------

40\. · 100% match · 2007 · 2.3 cit/yr\
**Synchronization of nonlinear systems under information constraints.** ([link](https://doi.org/10.1063/1.2977459))\
Alexander L. Fradkov, B. Andrievsky, and R. Evans\
*Chaos* · Dec 5, 2007 · 42 citations

> A brief survey of control and synchronization under information constraints (limited information capacity of the coupling channel) is given. Limit possibilities of nonlinear observer-based synchronization systems with first-order coders or full-order coders are considered in more detail. The existing and new theoretical results for multidimensional drive-response Lurie systems (linear part plus nonlinearity depending only on measurable outputs) are presented. It is shown that the upper bound of the limit synchronization error (LSE) is proportional to the upper bound of the transmission error. As a consequence, the upper and lower bounds of LSE are proportional to the maximum coupling signal rate and inversely proportional to the information transmission rate (channel capacity). The analysis is extended to networks having a “chain,” “star,” or “star-chain” topology. Adaptive chaotic synchronization under information constraints is analyzed. The results are illustrated by example: master-slave synchronization of two chaotic Chua systems coupled via a channel with limited capacity.

------------------------------------------------------------------------

41\. · 100% match · 1985 · 1.9 cit/yr\
**Tracking error bounds of adaptive nonstationary filtering** ([link](https://doi.org/10.1016/0005-1098(85%2990062-7))\
E. Eweda and O. Macchi\
*Autom.* · May 1, 1985 · 76 citations

------------------------------------------------------------------------

42\. · 99% match · 2007 · 3.5 cit/yr\
**Feedback Stabilization Over Signal-to-Noise Ratio Constrained Channels** ([link](https://doi.org/10.1109/TAC.2007.902739))\
J. Braslavsky, R. Middleton, and J. Freudenberg\
*IEEE Transactions on Automatic Control* · Aug 13, 2007 · 66 citations

------------------------------------------------------------------------

43\. · 98% match · 2018 · 1.0 cit/yr\
**Exploiting Timing Information in Event-Triggered Stabilization of Linear Systems With Disturbances** ([link](https://doi.org/10.1109/TCNS.2020.3030008))\
M. J. Khojasteh, Mojtaba Hedayatpour, J. Cortés, and M. Franceschetti\
*IEEE Transactions on Control of Network Systems* · May 5, 2018 · 8 citations

> Similar to the way pauses are used in spoken language to convey information, it is also possible to transmit information in communication networks not only by message content, but also with its timing. This article presents an event-triggering strategy that utilizes timing information by transmitting in a state-dependent fashion. We consider the stabilization of a continuous-time, time-invariant, linear plant over a digital communication channel with bounded delay and subject to bounded plant disturbances, and establish two main results. On the one hand, we design an encoding–decoding scheme that guarantees a sufficient information transmission rate for stabilization. On the other hand, we determine a lower bound on the information transmission rate necessary for stabilization by any control policy.

------------------------------------------------------------------------

44\. · 95% match · 2004 · 20 cit/yr\
**Stochastic linear control over a communication channel** ([link](https://doi.org/10.1109/TAC.2004.834430))\
S. Tatikonda, Anant Sahai, and S. Mitter\
*IEEE Transactions on Automatic Control* · Sep 13, 2004 · 442 citations

------------------------------------------------------------------------

45\. · 95% match · 2010 · 8.6 cit/yr\
**Minimum Data Rate for Mean Square Stabilization of Discrete LTI Systems Over Lossy Channels** ([link](https://doi.org/10.1109/TAC.2010.2054890))\
Keyou You and Lihua Xie\
*IEEE Transactions on Automatic Control* · Jun 28, 2010 · 137 citations

> This note investigates the minimum data rate for mean square stabilization of discrete linear time-invariant systems over a lossy channel. The packet dropout process of the channel is modeled as an independent and identically distributed process. For general single input systems, the minimum data rate is explicitly given in terms of unstable eigenvalues of the open loop matrix and the packet dropout rate, which clearly reveals the amount of the additional bit rate required to counter the effect of packet dropouts on stabilization. Sufficient data rate conditions for the mean square stabilization of multiple input systems are derived as well.

------------------------------------------------------------------------

46\. · 95% match · 1971 · 0.1 cit/yr\
**Linear Estimation in an Unknown Quasi-Stationary Environment** ([link](https://doi.org/10.1109/TSMC.1971.4308288))\
P. Monsen\
*IEEE Trans. Syst. Man Cybern.* · Jul 1, 1971 · 8 citations

> Linear estimation under a minimum mean-square-error criterion in a quasi-stationary environment is considered. A generalized form of the Widrow-Hoff algorithm is employed for the estimation. Performance is measured by the excess error over the minimum meansquare error. A Gaussian assumption is used to determine this performance and determine simple bounds. The transient solution for the algorithm is investigated and a convergence rate determined. These results are used to optimize the algorithm parameters and bound the performance as a function of the environmental rate of change. The Robbins-Monro algorithm for finding the root of a linear regression function suggests the use of fixed step size stochastic approximation algorithms to solve more general quasi-stationary estimation problems.

------------------------------------------------------------------------

47\. · 94% match · 2003\
**Mutual information rate and analytic constraint in linear time invariant control systems** ([link](https://www.semanticscholar.org/paper/fcfed67d3512d47fcfb4d517f88ab6762b263631))\
Zhang Hui\
0 citations

> Linear discretetime timeinvariant feedback systems disturbed by random processes are investigated from the viewpoint of information theory. Mutual information rate is employed as a measure of information transmission in systems to formulate the basic information condition of the tracking control problem. Based on this condition, a new design constraint is derived in dealing with the “information destruction” induced by exogenous disturbance input. Such analytic constraint indicates a relation between Bode integrals of the sensitivity function and the complementary sensitivity function, and implies a requirement of the unstable poles and nonminimum phase zeros of the open loop transfer function when it is strictly proper.

------------------------------------------------------------------------

48\. · 93% match · 2001 · 8.3 cit/yr\
**Information-theoretic approach to the study of control systems** ([link](https://doi.org/10.1016/j.physa.2003.09.007))\
H. Touchette and S. Lloyd\
*Physica A-statistical Mechanics and Its Applications* · Apr 2, 2001 · 209 citations

> We propose an information-theoretic framework for analyzing control systems based on the close relationship of controllers to communication channels. A communication channel takes an input state and transforms it into an output state. A controller, similarly, takes the initial state of a system to be controlled and transforms it into a target state. In this sense, a controller can be thought of as an actuation channel that acts on inputs to produce desired outputs. In this transformation process, two different control strategies can be adopted: (i) the controller applies an actuation dynamics that is independent of the state of the system to be controlled (open-loop control); or (ii) the controller enacts an actuation dynamics that is based on some information about the state of the controlled system (closed-loop control). Using this communication channel model of control, we provide necessary and sufficient conditions for a system to be perfectly controllable and perfectly observable in terms of information and entropy. In addition, we derive a quantitative trade-off between the amount of information gathered by a closed-loop controller and its relative performance advantage over an open-loop controller in stabilizing a system. This work supplements earlier results (Phys. Rev. Lett. 84 (2000) 1156) by providing new derivations of the advantage afforded by closed-loop control and by proposing an information-based optimality criterion for control systems. New applications of this approach pertaining to proportional controllers, and the control of chaotic maps are also presented.

------------------------------------------------------------------------

49\. · 92% match · 2005\
**The Information Cost of Loop Shaping over** ([link](https://www.semanticscholar.org/paper/6dbf4aa389f9b643837652cfbe4577c29fa79e1e))\
G. Channels\
0 citations

> In this paper, we extend the results of our previous work on feedback stabilization and feedback com- munication to include the presence of an external input acting as a output disturbance on the feedback system. Rather than on the communication system, we focus on the control system. We show that the Directed Information still characterizes the information rate flowing through the channel, and that it is constant for a given open loop Degree of Instability and the channel model. This indicates that, in our case, loop shaping does not affect the rate through the channel but only the transmission power if the degree of instability is kept constant. For the memoryless AWGN channel we characterize the required transmission power in a closed form which relates a function of the required transmission power to the sum two rates: one given by the Directed Information, the other lost due to the non flat frequency shaping of the Sensitivity and expressed in term of a relative entropy. This result provides a new interpretation to the H∞ Sensitivity minimization problem which is based on information theoretic concepts.

------------------------------------------------------------------------

50\. · 91% match · 2012 · 0.1 cit/yr\
**Networked Control Systems with Unbounded Noise under Information Constraints** ([link](https://www.semanticscholar.org/paper/0fe4d854f7d368253ea1dbf223ced3c82d917905))\
Andrew P. Johnston\
Dec 6, 2012 · 1 citations

> We investigate the stabilization of unstable multidimensional partially observed singlestation, multi-sensor (single-controller) and multi-controller (single-sensor) linear systems controlled over discrete noiseless channels under fixed-rate information constraints. Stability is achieved under communication requirements that are asymptotically tight in the limit of large sampling periods. Through the use of similarity transforms, sampling and random-time drift conditions we obtain a coding and control policy leading to the existence of a unique invariant distribution and finite second moment for the sampled state. We use a vector stabilization scheme in which all modes of the linear system visit a compact set together infinitely often.

*Showing top 50 of 103 papers. Full details available via CSV or BibTeX export.*
