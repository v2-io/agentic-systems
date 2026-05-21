# Prior-Art Analysis: Coordinate Forcing via Uniqueness Theorems

**Target Claim:**
AAT employs a distinct meta-methodology for constructing its theoretical scaffolding: it does not arbitrarily select loss functions, distance metrics, or update rules. Instead, it leverages classical mathematical *uniqueness theorems* (and impossibility/no-go theorems) as constructive tools to "force" the exact coordinates of the framework. Specifically, the framework forces:
1. The update operator to be reverse-Kullback-Leibler (via Shore-Johnson/Caticha axioms).
2. The divergence measure to be Kullback-Leibler (as the unique intersection of $f$-divergences and Bregman divergences via Amari).
3. The geometric tensors to be the Fisher Information metric and the Amari-Chentsov tensor (via Chentsov/Ay invariance under sufficient statistics).

---

## 1. State of the Field & Scientific Precedence

The Undermind search demonstrates that the mathematical components of AAT's "coordinate forcing" are backed by some of the most profound and celebrated uniqueness theorems in statistics and information geometry. While the practice of deriving rules axiomatically has a long history, AAT's explicit meta-methodological stance—using these theorems en masse to rigidly lock down an entire cognitive architecture—represents a powerful theoretical synthesis.

### Pillar 1: Uniqueness of the Update Operator (Shore-Johnson & Caticha)
The claim that the agent's belief-update rule is strictly forced into a specific entropic form (reverse-KL/Maximum Relative Entropy) is anchored by **Shore and Johnson (1980)**. They proved that maximizing entropy (and minimizing cross-entropy/KL divergence) is the *unique* method of inductive inference that satisfies four basic axioms of logical consistency (e.g., coordinate invariance, subset independence). **Caticha (2006, 2021)** expanded this specifically for Bayesian agents, proving via an eliminative induction process that the logarithmic relative entropy is the unique, universally applicable tool for updating probabilities that respects the value of prior information.

### Pillar 2: Uniqueness of the Divergence Function (Amari & Csiszár)
Why does the agent measure prediction mismatch (divergence) the way it does? AAT relies on the uniqueness of the Kullback-Leibler divergence. **Amari (2009)** proved a landmark theorem in information geometry: among all possible divergence measures, the $\alpha$-divergence is the *only* one that belongs to both the class of $f$-divergences (which maintain information monotonicity under coarse-graining) and Bregman divergences (which give dually flat geometries). Within this, KL divergence is the unique intersection in the manifold of probability distributions. **Csiszár (1991)** provided parallel axiomatic characterizations of why specific distance functions (like I-divergence) are logically forced in inverse problems.

### Pillar 3: Uniqueness of the Geometric Tensors (Chentsov & Ay)
When the agent represents its model space geometrically, the choice of metric is forced. Classical results by Chentsov proved that the Fisher Information matrix is the unique Riemannian metric (up to a constant) that is invariant under Markov morphisms (sufficient statistics). **Ay, Jost, Lê, and Schwachhöfer (2012, 2015)** rigorously extended this uniqueness theorem to infinite-dimensional sample spaces (parameterized measure models). They proved that the Fisher metric and the Amari-Chentsov tensor are the *only* geometric structures that survive transformation by sufficient statistics without losing information, forcing any rational agent's internal geometric representation to adopt these exact tensors.

---

## 2. Key Anchor Papers (Available in `/ref`)

The following seminal papers establish the exact mathematical uniqueness proofs upon which AAT relies. (These have been located in the `ref/` directory):

1. **Shore, J., & Johnson, R. W. (1980). Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy.** (`ref/shore-johnson-1980-axiomatic-maxent.pdf`)
   *Significance:* The bedrock proof that logical consistency under coordinate transformations uniquely forces the use of cross-entropy (KL divergence) for updating beliefs.
2. **Amari, S. (2009). $\alpha$-Divergence Is Unique, Belonging to Both $f$-Divergence and Bregman Divergence Classes.** (`ref/amari-2009-alpha-divergence-unique-f-bregman.pdf`)
   *Significance:* The definitive geometrical proof that locks in the specific divergence function by showing it is the sole mathematical intersection of two mandatory structural properties (monotonicity and dual-flatness).
3. **Ay, N., Jost, J., Lê, H., & Schwachhöfer, L. (2012). Information geometry and sufficient statistics.** (`ref/ay-2017-information-geometry.pdf`)
   *Significance:* Generalizes Chentsov's theorem, proving the absolute uniqueness of the Fisher metric and Amari-Chentsov tensor for statistical models based on the requirement of invariance under sufficient statistics.
4. **Csiszár, I. (1991). Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems.** (`ref/csiszar-1991-why-least-squares-maxent.pdf`)
   *Significance:* Provides independent axiomatic justification for why these specific projection and optimization geometries are uniquely mandated for inference.

---

## 3. Conclusion on Novelty & Overlap

The underlying mathematical theorems (Shore-Johnson, Amari, Chentsov/Ay) are established canonical facts within Information Geometry and Maximum Entropy physics. AAT claims no novelty in inventing these theorems.

**AAT's Novel Contribution:** The novelty lies entirely in the **epistemological architecture**. Most machine learning and cognitive architectures treat their loss functions, metrics, and update rules as *hyperparameters*—choices engineered for empirical performance (e.g., choosing Huber loss over MSE, or Wasserstein distance over KL). 

AAT argues that for an autonomous, theoretically optimal agent, these cannot be choices. By assembling this specific chain of uniqueness theorems, AAT demonstrates that an agent's internal cognitive coordinate system is physically and logically "forced." AAT's meta-methodological claim—using "coordinate forcing" to strip away all degrees of freedom in the agent's foundational math—is a highly rigorous and novel way to construct a unified theory of agency.