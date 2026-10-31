# Macro-Symbiotic Tensor ($O_0 \to O_\Omega$): Design Rationale & Notation Companion
**Companion to:** `foundational-manifold-2026-10-20-r7.json` (companion revision r10). The r7 JSON generalizes r6 under Design Decision 6; every r6 equation is recovered as the Branch I default, and §5.1–§5.12 below verify that case. §5.1–§5.12 are unchanged from r9 except one correction: the reference-prior normalization of §5.4 (and the overlap density of §5.8) is now stated in the $\sqrt{\vert g\vert}$-weighted form, which repairs the prior that §5.10 and §5.11 inherit from §5.4, where $Q$ is non-uniform and r9's unweighted condition did not normalize $P$.

## 1. Purpose of This Document
This companion document records the modeling decisions, physical intuition, and standardized mathematical notation underlying the nine-coordinate specification in `foundational-manifold-2026-10-20-r7.json` (and its r6 special case). It connects the systems-theoretic intent of the framework to the differential-geometric equations.

---

## 2. Core Modeling Decisions & Design Rationale

### Decision 1: Homothetic (Conformally Stationary) Closure at the Asymptote ($O_\Omega \to O_0$)
* **Conceptual Intent:** The system is permanently open to environmental flux ($\dot{W}_{\mathrm{ext}} > 0$) and continuously expands its capacity, yet at the asymptotic horizon ($O_\Omega$) it achieves a stable, stationary form that closes the loop back to $O_0$.
* **Mathematical Implementation:** A metric cannot be strictly static ($\partial_\tau g_{\mu\nu} = 0$) while its volume is still growing ($\theta = \nabla_\mu J_{\mathrm{geom}}^\mu > 0$, Branch I). Therefore, $O_\Omega$ is modeled as a **homothetic (self-similar) state**: as $\tau \to \infty$, the expansion scalar approaches a positive constant ($\theta \to n H_0 > 0$) while internal shear decays to zero ($\sigma^\mu_{\;\nu} \to 0$). The physical volume grows without bound ($V_{\mathcal{M}}(\tau) \sim e^{n H_0 \tau} \to \infty$; precisely, $e^{-2H_0\tau}g_{\mu\nu} \xrightarrow{C^2(\mathcal{M})} G_{\infty,\mu\nu} \succ 0$ by $O_5$ Eq. 4), sustaining positive boundary work ($\dot{W}_{\mathrm{ext}} > 0$), while the **conformally rescaled metric** $\tilde{g}_{\mu\nu} = \Omega^{-2}g_{\mu\nu} \to \hat{g}_\infty$ becomes time-independent ($\partial_\tau \tilde{g}_{\mu\nu} \to 0$).
* **Mixed-Index Limit:** Because the lower-index metric components $g_{\mu\nu}$ grow as $e^{2H_0\tau}$ (with $e^{-2H_0\tau}g_{\mu\nu} \to G_{\infty,\mu\nu}$, so the Christoffel symbols stay bounded in $C^1$), asymptotic convergence in $O_\Omega$ is written in mixed $(1,1)$ form ($\frac{1}{2}g^{\mu\alpha}\partial_\tau g_{\alpha\nu} \to H_0 \delta^\mu_\nu$), which is scale-invariant.

### Decision 2: Separating Extrinsic Expansion ($\theta, K_{\mu\nu}$) from Environmental Stiffness ($\Pi_{\mu\nu}$) ($O_0, O_2, O_3$)
* **Conceptual Intent:** Navigating a rigid external environment ($O_2$) should guide trajectories without crushing internal growth ($O_3$).
* **Mathematical Implementation:**
  1. **Synchronous Normal Gauge ($N = 1, \beta^\mu = 0$):** All volumetric growth is carried once by the normal extrinsic expansion scalar $\theta \equiv -N K = \frac{1}{2}g^{\mu\nu}\partial_\tau g_{\mu\nu} = \nabla_\mu J_{\mathrm{geom}}^\mu \ge 0$ ($> 0$ in Branch I; r6 wrote $\nabla_\mu J_E^\mu$, and Decision 6 separates the currents), avoiding any double-counting between coordinate velocity and metric growth.
  2. **Unimodular Conformal-Weyl Factorization:** The spatial metric is factored non-perturbatively as $g_{\mu\nu} = \Omega^2 \hat{g}_{\mu\alpha}(\exp \hat{h})^\alpha_{\;\nu}$ with $\det \hat{g} = 1$ and $\mathrm{Tr}(\hat{h}) = 0$. Because $\det(\exp \hat{h}) = 1$ at all finite shear amplitudes, the volume element $\sqrt{\vert g\vert} = \Omega^n$ depends *only* on the conformal factor $\Omega$ (a scalar density of weight $1/n$ in the fixed reference chart), isolating the volume element from anisotropic shear ($\hat{h}$). The factorization is a change of variables, so it does **not** decouple $\theta$ from environmental stiffness: since $R = \kappa_G \nabla_\alpha \xi^\alpha$ with $\xi_\alpha = \hat{\Pi}_{\alpha\lambda}\eta^\lambda$, the trace of the $\tau$-compatibility law gives the elliptic equation $\frac{2(n-1)}{n}\nabla^2\theta + \frac{2R}{n}\theta = -\kappa_G\,\partial_\tau(\nabla_\alpha\xi^\alpha) + 2\nabla^\alpha\nabla^\beta\sigma_{\alpha\beta} - 2\sigma^{\alpha\beta}R_{\alpha\beta}$, which ties expansion to precision.

### Decision 3: Local Subsystem Metrics ($g^{(i)}$) vs. the Glued Macroscopic Metric ($g \equiv g^{\mathrm{macro}}$) ($O_3 \to O_5$)
* **Conceptual Intent:** Individual subsystems ($O_4$) bring distinct internal geometries ($g^{(i)}$) into shared overlap zones ($O_5$), blending them into a coherent macroscopic whole ($O_7$).
* **Mathematical Implementation:**
  1. **Fixed Open Cover ($\mathcal{M} = \bigcup_i \mathcal{U}_i$):** The coordinate domains $\mathcal{U}_i$ and their intersections $\mathcal{U}_{ij} = \mathcal{U}_i \cap \mathcal{U}_j$ are fixed in coordinate space, while their *physical Riemannian volumes* ($\int \sqrt{\vert g^{(i)}\vert}\,d^n x$) dilate over time. This allows the Reynolds transport theorem in $O_4$ to hold cleanly without moving-coordinate-boundary terms.
  2. **Riemannian Geometric Mean ($g^{(i)} \# g^{(j)}$):** On each overlap $\mathcal{U}_{ij}$, the two subsystem metrics are interpolated via their positive-definite geometric mean $g_{\mu\nu}^{(ij)} = (g^{(i)} \# g^{(j)})_{\mu\nu}$ and glued over all geometric overlaps $\mathcal{K}_0 = \{\langle i,j\rangle : \mathcal{U}_i \cap \mathcal{U}_j \neq \emptyset\}$ via a smooth, time-independent partition of unity ($\psi_i, \psi_{ij} \ge 0$) into the single global metric $g_{\mu\nu} \equiv g_{\mu\nu}^{\mathrm{macro}}$. Percolation is measured separately on the actively coupled subgraph $\mathcal{K} = \{\langle i,j\rangle \in \mathcal{K}_0 : \eta_{[i\to j]} \not\equiv 0\}$ through the fraction $\phi_{\mathrm{perc}}(\mathcal{K}) = \vert\mathcal{K}\vert/\vert\mathcal{K}_0\vert > \phi_c$.
  3. **Avoiding Overdetermination:** The exact differential evolution laws ($O_2$–$O_4$) are imposed on the glued global metric $g_{\mu\nu}$, while individual subsystem metrics $g_{\mu\nu}^{(i)}$ carry, as standing hypotheses, the asymptotic homothety conditions with a common expansion rate $H_0$ ($e^{-2H_0\tau}g^{(i)}_{\mu\nu} \to G^{(i)}_{\infty,\mu\nu} \succ 0$ and $\frac{1}{2}(g^{(i)})^{\mu\alpha}\partial_\tau g^{(i)}_{\alpha\nu} \to H_0\delta^\mu_\nu$, both in $C^2(\mathcal{U}_i)$). The glued metric inherits them, $e^{-2H_0\tau}g_{\mu\nu} \xrightarrow{C^2(\mathcal{M})} G_{\infty,\mu\nu} \succ 0$ ($O_5$ Eq. 4); $O_6$ uses this for the volume shares $c_{ij} \in (0,1]$ and $O_\Omega$ uses it to bound the Christoffel symbols. The tilde is reserved for the unit-determinant rescaling $\tilde{g}_{\mu\nu} = \Omega^{-2}g_{\mu\nu} \to \hat{g}_{\infty,\mu\nu}$; the $e^{-2H_0\tau}$-rescaled limits are written $G_\infty$.

### Decision 4: Pairwise Joint Density ($Q_{ij}$), Overlap Divergence ($Q_i^{\vert ij}$), and Asymmetric Lead-Follow Coupling ($\eta_{[i\to j]}$) ($O_6$)
* **Conceptual Intent:** Coupled partners should sustain positive mutual information flow ($\frac{d}{d\tau}\mathcal{I} > 0$) through an asymmetric coupling ($\eta_{[i\to j]} \not\equiv 0$), even as their local states align ($D_{\mathrm{KL}} \to 0$). Only the *magnitude* of the asymmetry enters the dynamics; the equations cannot tell which partner leads.
* **Mathematical Implementation:**
  1. **Joint vs. Overlap-Conditional Distributions:** Each pair of coupled subsystems carries a joint distribution $Q_{ij}$ on $\mathcal{U}_i \times \mathcal{U}_j$ with marginals $Q_i$ and $Q_j$, defining mutual information $\mathcal{I}(Q_i; Q_j) = D_{\mathrm{KL}}(Q_{ij} \parallel Q_i \otimes Q_j)$. Meanwhile, distributional alignment is measured on their shared overlap $\mathcal{U}_{ij}$ via normalized conditional densities $Q_i^{\vert ij}$, allowing $D_{\mathrm{KL}}(Q_i^{\vert ij} \parallel Q_j^{\vert ij}) \to 0$ while $\mathcal{I}(Q_i; Q_j)$ continues to grow.
  2. **Quadratic Asymmetric Coupling in $M_{\mu\nu}^{(ij)}$:** To ensure the antisymmetric phase-lead $\eta_{[i\to j]}^\lambda = \frac{1}{2}(\eta_{i\to j}^\lambda - \eta_{j\to i}^\lambda)$ drives the stretching-and-folding operator $M_{\mu\nu}^{(ij)}$ even when two partners have identical precision stiffness ($\hat{\Pi}^{(i)} = \hat{\Pi}^{(j)}$), $M_{\mu\nu}^{(ij)}$ includes a trace-free quadratic term in the precision-symmetrized phase-lead 1-form $J_{[i\to j]} = -J_{[j\to i]}$. This 1-form is odd under $i \leftrightarrow j$ (its sign records the leader), but it enters $M^{(ij)}$ only through its even outer product, so $M^{(ij)}$, $S^{(ij)}$, and $d\mathcal{I}/d\tau$ are leader-follower symmetric. It generally differs from $\frac{1}{2}(J_{i\to j} - J_{j\to i})$, with equality when $\hat{\Pi}^{(i)} = \hat{\Pi}^{(j)}$. Because the quadratic term can still cancel against the conformal-Killing term, $M^{(ij)}(\mathbf{x}) \neq 0 \; \forall \mathbf{x} \in \bar{\mathcal{U}}_{ij}$ and $d\mathcal{I}/d\tau > 0$ are stated as explicit hypotheses. Since $\mathrm{Tr}\,M^{(ij)} = 0$, the mixed eigenvalues have both signs and sum to zero ($m_+ > 0 > m_-$); they need not be equal in magnitude.

### Decision 5: Smooth Anisotropy Index ($\chi$) and Type-$(1,1)$ Density Endomorphisms ($\hat{\rho}_g, \hat{\rho}_{\mathcal{H}}$) ($O_7$)
* **Conceptual Intent:** The macroscopic network relaxes its deformation toward isotropy ($\chi \to 1$), tracked covariantly by a gauge field, and aligns its active geometry ($g_{\mu\nu}$) with its accumulated structural memory ($\mathcal{H}$). (Local stretching and folding belong to the relational edge, $M^{(ij)}$ in $O_6$; $\chi$ measures the anisotropy of the global deformation $\mathcal{D}$.)
* **Mathematical Implementation:**
  1. **$C^2$, Kink-Free Anisotropy Scalar:** Instead of a ratio of maximum-to-minimum eigenvalues (which creates non-differentiable kinks where eigenvalues cross), anisotropy is measured by the kink-free invariant $\chi \equiv \frac{n\,\mathrm{Tr}(\mathcal{D}^2)}{(\mathrm{Tr}\,\mathcal{D})^2} = 1 + \frac{n\,\sigma^\mu_{\;\nu}\sigma^\nu_{\;\mu}}{\theta^2} \ge 1$, which is $C^2$ (it inherits the regularity of $\partial_\tau g_{\mu\nu} \in C^2$) and converges to $1$ as shear decays (Branch I, where $\theta \to nH_0 > 0$; in Branch II the index is $\chi_E$, Decision 6).
  2. **Type-$(1,1)$ Endomorphisms for Relative Entropy:** Because matrix logarithms and traces are only coordinate-invariant for $(1,1)$ mixed tensors, $g_{\alpha\nu}$ and $\nabla_\alpha \nabla_\nu \mathcal{H}$ have their first index raised by the asymptotic inverse reference metric $\hat{g}_\infty^{\mu\alpha}$ (the density weights cancel in the normalized ratio) to form unit-trace density operators $(\hat{\rho}_g)^\mu_{\;\nu}$ and $(\hat{\rho}_{\mathcal{H}})^\mu_{\;\nu}$.

### Decision 6: Throughput Separated from Expansion; Declared Drive, Transport, and Sink; Two Asymptotic Branches (r7, r10)
**Motivation.** In r6, one current $J_E^\mu$ both expands the metric volume ($\theta = \nabla_\mu J_E^\mu > 0$) and carries the free-energy throughput ($J_E^\mu\nabla_\mu\mathcal{F} < 0$), the free-energy balance law has isotropic constant diffusivity and no interior sink, test trajectories are force-free, and the asymptote requires unbounded homothetic expansion ($H_0 > 0$). These are the laws of a homogeneous, sink-free, perpetually inflating medium. Bounded open systems with interior consumption, anisotropic transport, or driven trajectories cannot satisfy them literally. r7 generalizes exactly these points and nothing else.

**What changes (r7).** Eighteen equation blocks are edited; all other blocks are unchanged.
1. **Expansion versus throughput** ($O_0$ Eq. [1], [3], [4]; $O_1$ Eq. [0], [1]; $O_2$ Eq. [2]; $O_3$ Eq. [1]; $O_4$ Eq. [3]; $O_6$ Eq. [4]; $O_7$ Eq. [3]). Every r6 identity of the form $\theta = \nabla_\mu J_E^\mu$ now reads $\theta = \nabla_\mu J_{\mathrm{geom}}^\mu$, including $\partial_\tau\ln\Omega = \theta/n$ ($O_2$ Eq. [2]) and the $u_{\mathrm{exp}}$ flux identity ($O_7$ Eq. [3]); statements of $\theta > 0$ carry the qualifier "$> 0$ in Branch I". Three currents are distinguished:
   * $J_{\mathrm{geom}}^\mu$, the expansion current: $\theta = \nabla_\mu J_{\mathrm{geom}}^\mu \ge 0$ and $dV_{\mathcal{M}}/d\tau = \oint J_{\mathrm{geom}}^\mu\,d\Sigma_\mu$.
   * $J_W^\alpha = -\mathfrak{K}^{\alpha\beta}\nabla_\beta\mathcal{F}$, the free-energy transport current of $O_4$.
   * $J_E^\mu$, the throughput current entering $O_0$ Eq. [2] (hysteresis) and $O_1$: in Branch I, $J_E^\mu \equiv J_{\mathrm{geom}}^\mu$ (the r6 identification); in Branch II, $J_E^\mu \equiv J_W^\mu/p_0$ is fixed (no alternative is admitted, so a declared throughput current cannot be used to satisfy $O_0$ Eq. [2], $O_1$, or the $O_\Omega$ generator condition by construction), for which $J_E^\mu\nabla_\mu\mathcal{F} = -p_0^{-1}\nabla\mathcal{F}\cdot\mathfrak{K}\cdot\nabla\mathcal{F} < 0$ holds identically wherever $\nabla\mathcal{F} \neq 0$.

   Non-equilibrium openness is carried in both branches by $\Theta_E \equiv \dot{s}_{\mathrm{prod}}/s_0$ (a rate, since $\dot{s}_{\mathrm{prod}}$ is an entropy production density and $s_0$ an entropy density). $O_0$ Eq. [1] only defines $\Theta_E$, $\Theta_{\mathrm{tot}}$, and $\tau_\Theta$; their positivity and monotonicity are stated in $O_0$ only as consequences of the $O_1$ Eq. [1] sign condition, so under the defaults $O_0$ imposes nothing beyond r6's $O_0$. Events are ordered by $\tau_\Theta(\tau) = \int_{\tau_0}^\tau\langle\Theta_{\mathrm{tot}}\rangle_{\mathcal{M}}\,d\tau'$ with $\Theta_{\mathrm{tot}} = \sqrt{\theta^2 + \Theta_E^2} > 0$. $\tau_\Theta$ is dimensionless (when $\theta = 0$, it is the count of entropy production per $s_0$); $\tau$ remains the proper time of normal observers, and $\tau_\Theta$ is a strictly monotone reparametrization of it. In Branch I both $\theta$ and $\Theta_E$ drive $\tau_\Theta$ (r6 stated no such clock), and in Branch II $\Theta_E$ alone does. Power splits into expansion work $\dot{W}_{\mathrm{ext}} = p_0\dot{V}_{\mathcal{M}} \ge 0$ (unchanged symbol and formula, $> 0$ in Branch I) and dissipative power $\dot{W}_{\mathrm{diss}} = \int(-J_E^\mu\nabla_\mu\mathcal{F})\sqrt{\vert g\vert}\,d^nx > 0$, with $\dot{W}_{\mathrm{tot}} > 0$. Keeping $\dot{W}_{\mathrm{ext}}$ as pure expansion work, rather than redefining it as the sum, is what keeps r6's $O_1$ Eq. [0] intact as the Branch I case.
2. **Declared drive** ($O_2$ Eq. [3]; $a_{\mathrm{d}}$ jointly continuous and locally Lipschitz in $(\mathbf{x}, v)$ locally uniformly in $\tau$, with $\Gamma$ and $g^{-1}\partial_\tau g$ locally Lipschitz in $\mathbf{x}$ locally uniformly in $\tau$, e.g. $\partial_{\mathbf{x}}\Gamma$ and $\partial_{\mathbf{x}}\partial_\tau g$ jointly continuous, so the whole right side is locally Lipschitz and solutions are unique; joint continuity alone gives existence, not uniqueness). The trajectory equation carries $f^\mu_{\mathrm{drive}} = (1-u^2)\big(a^\mu_{\mathrm{d}} - (a_{\mathrm{d}}\cdot v)v^\mu\big)$ on its right side, with $u^2 = g_{\mu\nu}v^\mu v^\nu$ and a declared drive acceleration $a^\mu_{\mathrm{d}}$ (zero by default). This projected form is required: an unrestricted drive can push trajectories through $u^2 = 1$, since along solutions $du^2/d\tau = -(1-u^2)\,\partial_\tau g_{\rho\epsilon}v^\rho v^\epsilon + 2\,g_{\mu\nu}v^\mu f^\nu$. With the projected form, $g_{\mu\nu}v^\mu f^\nu = (1-u^2)^2(a_{\mathrm{d}}\cdot v)$, so $du^2/d\tau$ carries a factor $(1-u^2)$, $u^2 = 1$ is invariant, and the timelike condition $u^2 < 1$ is preserved.
3. **Declared transport and sink** ($O_4$ Eq. [1]). $\partial_\tau\mathcal{F} + \mathcal{F}\theta = -\nabla_\alpha J_W^\alpha - \mathcal{R}_{\mathcal{F}}$ with $J_W^\alpha = -\mathfrak{K}^{\alpha\beta}\nabla_\beta\mathcal{F}$, $\mathfrak{K} \succ 0$ symmetric, and $\mathcal{R}_{\mathcal{F}} \ge 0$. The defaults $\mathfrak{K}^{\alpha\beta} = D_{\mathcal{F}}g^{\alpha\beta}$ and $\mathcal{R}_{\mathcal{F}} = 0$ recover r6.
4. **Anisotropy index** ($O_7$ Eq. [5]). $\chi = n\,\mathrm{Tr}(\mathcal{D}^2)/(\mathrm{Tr}\,\mathcal{D})^2$ is unchanged and remains the Branch I index; its identity with $1 + n\sigma\sigma/\theta^2$ follows from $\mathcal{D} = \frac{\theta}{n}\delta + \sigma$ and must not be altered. A separate index $\chi_E \equiv 1 + n\,\sigma^\mu_{\;\nu}\sigma^\nu_{\;\mu}/(\theta^2 + \langle\Theta_E\rangle_{\mathcal{M}}^2)$ is defined in both branches; it is not $n\,\mathrm{Tr}(\mathcal{D}^2)/(\mathrm{Tr}\,\mathcal{D})^2$, satisfies $1 \le \chi_E \le \chi$ wherever $\theta > 0$, and tends to $1$ whenever $\sigma \to 0$ and $\liminf\langle\Theta_E\rangle_{\mathcal{M}} > 0$. In Branch II the adjoint section is $\hat{\chi} = \chi_E\hat{u}$.
5. **Two asymptotic branches** ($O_5$ Eq. [0] and [4]; $O_\Omega$ Eq. [0]–[2]).
   * **Branch I** ($H_0 > 0$) is the r6 homothetic horizon, unchanged.
   * **Branch II** ($H_0 = 0$) is a bounded non-equilibrium steady state: $\theta \to 0$ with $\int_{\tau_0}^\infty\langle\theta\rangle\,d\tau < \infty$, so $V_{\mathcal{M}} \to V_\infty < \infty$ and $\mathcal{I} \to s_0V_\infty$ (finite capacity); $\langle\Theta_E\rangle_{\mathcal{M}} \to \Theta_\infty > 0$; $\sigma \to 0$; $\partial_\tau g_{\mu\nu} \to 0$.
   * The homothety hypotheses of $O_5$ Eq. [4] and the derived limits of $O_6$ Eq. [4] and $O_\Omega$ Eq. [1] hold for $H_0 \ge 0$. At $H_0 = 0$: $g^{(i)} \to G^{(i)}_\infty$ in $C^2$ and $\frac{1}{2}(g^{(i)})^{-1}\partial_\tau g^{(i)} \to 0$ are the hypotheses; smoothness and homogeneity of $\#$ carry both to the glued metric; the volume shares converge, giving $c_{ij}$; and $C^2$ convergence of $g$ bounds the Christoffel symbols and curvature, giving the $O_\Omega$ Eq. [1] limits. The Branch II premise $\int\langle\theta\rangle\,d\tau < \infty$ is implied by $g \to G_\infty$ and is retained for explicitness.
   * In Branch II, $\mathcal{I}(\tau) \to s_0V_\infty < \infty$ while $d\mathcal{I}/d\tau > 0$ (hypothesis), so the $O_6$ coupling-tensor boundary flux must be integrable on $[\tau_0, \infty)$. The $O_6$ Eq. [3] hypothesis $M^{(ij)} \neq 0$ at every finite $\tau$ remains compatible with this, since the flux need only be integrable; it tends to $0$ under the additional hypothesis that it is uniformly continuous in $\tau$ (Barbalat's lemma). r7 states this in the $O_6$ and $O_\Omega$ branch-scope fields.
   * The $O_\Omega$ generator equivalence divides by $nH_0$ and therefore holds in Branch I only, where (as in r6 and §5.10) it holds at every $\tau$. In Branch II the first term of $\hat{\mathbb{L}}_{\mathrm{stat}}$ vanishes at every $\tau$, so imposing $\hat{\mathbb{L}}_{\mathrm{stat}}\Psi = 0$ at every $\tau$ would forbid all surprisal transduction. r7 therefore states the Branch II condition asymptotically: with $\vert\delta\Psi/\delta\mathcal{H}\vert$ bounded and bounded away from $0$, uniformly as $\tau \to \infty$ (the lower bound gives the forward implication, the upper bound the reverse), $\hat{\mathbb{L}}_{\mathrm{stat}}\Psi\vert_{\mathcal{H}_{\mathrm{sol}}} \to 0 \iff J_E^\lambda\nabla_\lambda q \to 0 \iff \partial_\tau\mathcal{H} \to 0$ as $\tau \to \infty$. The Branch II fixed point is asymptotically stationary hysteresis, and surprisal transduction at finite $\tau$ is permitted.
   * Statements that hold in Branch I only: $O_5$ Eq. [0]'s strict growth $\partial_\tau\sqrt{\vert g^{(i)}\vert} > 0$ (now $\ge 0$, with $> 0$ in Branch I), $O_0$ Eq. [4] ($V_{\mathrm{field}} = \infty$), the $O_1$ "integrates" edge (unbounded boundary flux), the $\chi \to 1$ implication of $O_7$ Eq. [5] (whose premise is $\theta \to nH_0 > 0$), the deformation-spectrum hypothesis $\lambda_{\min}(\mathcal{D}) > 0$ of $O_6$ Eq. [4] (a standing hypothesis in Branch I, as in r6; not asserted in Branch II, where $\mathcal{D} \to 0$), the definition of $\chi$ itself (undefined where $\theta = 0$), and the $nH_0$ form of the $O_\Omega$ generator equivalence. Each coordinate of r7 carries an `r7_branch_scope` field stating this. Several relational edges were updated to state r7 formulas or carry branch labels; all other retained r6 prose and edges, including r6 clauses retained alongside r7 formulas within an edge, describe Branch I with the default constitutive terms, as each `r7_branch_scope` field states.

**Constitutive closure (Amendment A; binding text in r7 $O_4$, field `r7_constitutive_closure`).** The new terms make the spine more general, so they must not make it unfalsifiable. Any departure from the defaults ($a^\mu_{\mathrm{d}} = 0$, $\mathfrak{K}^{\alpha\beta} = D_{\mathcal{F}}g^{\alpha\beta}$, $\mathcal{R}_{\mathcal{F}} = 0$; the Branch II $J_E^\mu = J_W^\mu/p_0$ is fixed and admits no departure) must satisfy four conditions: (i) its functional form is a named constitutive law fixed before the test (for example a potential gradient or drag law for $f_{\mathrm{drive}}$, a measured conductivity or permeability tensor for $\mathfrak{K}$, first- or zeroth-order kinetics for $\mathcal{R}_{\mathcal{F}}$); (ii) it has a finite number of parameters declared in advance (tabulated or non-parametric fields are not admissible), estimated from data independent of the test and not merely disjoint in time: a different measurement modality from the one used to test the coordinate, or a declared perturbation or non-stationary regime distinct from the test window (temporal disjointness alone is not independence in a stationary Branch II state, where a later window re-measures an earlier one); (iii) every acceptance tolerance and comparison criterion is fixed before the test; (iv) the default model is fitted to the same test-window data and its residual reported alongside, and if the default fits at least as well under the pre-declared criterion, the departure is rejected and the coordinate is evaluated under the default. The test-window fit of the default is used only for the comparison of (iv): whenever a coordinate is evaluated under the default, its parameters are estimated per (ii), from data independent of the test. A term fitted to the data it closes does not count as satisfying any coordinate in which the term appears. In Branch II, with the fixed $J_E^\mu$, the $O_1$ sign condition holds identically; the empirical content of $O_1$ is then that the declared parametric $\mathfrak{K}$, with parameters estimated per (ii), predicts the flux: the independently measured free-energy flux $J_W^{\mathrm{meas}}$ (measured directly, within the test window, across a declared surface, by a method that does not use the declared $\mathfrak{K}$) agrees with $-\mathfrak{K}^{\alpha\beta}\nabla_\beta\mathcal{F}$ within the pre-declared tolerance. The gradient $\nabla\mathcal{F}$ in this comparison must be obtained within the test window by a method that uses neither $J_W^{\mathrm{meas}}$ nor the declared $\mathfrak{K}$ or $\mathcal{R}_{\mathcal{F}}$; otherwise the agreement is automatic. The compared quantity is pre-declared: the total flux through the declared surface $S$, or the normal flux density pointwise on $S$. Every evaluation, under the defaults or a declared departure, also requires condition (v): the branch is declared before the test, with a pre-declared estimator and acceptance criterion for the asymptotic regime (an estimate of $H_0 > 0$ for Branch I; the trend of $\langle\theta\rangle$, a bound on $\int\langle\theta\rangle\,d\tau$, and an estimate of $\lim\langle\Theta_E\rangle > 0$ for Branch II), supported by evidence independent of the $O_1$ test, and a configuration declared in one branch may not be re-evaluated in the other on the same data. Clause (v) matters because the branch switches $J_E$, and with it the content of $O_1$ (a sign test in Branch I, a flux-prediction test in Branch II) and the anisotropy index of $O_7$.

**Scope of verification.** §5.1–§5.12 verify the Branch I default and are unchanged except for the normalization correction noted in the header. §5.13 constructs and verifies one Branch II witness. Nothing in r10 claims that the generalized system is jointly satisfiable beyond what those sections verify.

---

## 3. Standing Hypotheses (r3, extended in r4–r6)
Regularity: $g_{\mu\nu}, g^{(i)}_{\mu\nu} \in C^3$, $\partial_\tau g_{\mu\nu} \in C^2$, $\Phi, \Phi^{(j)} \in C^4$, $\eta, \eta_{i\to j} \in C^2$, $\psi \in C^\infty$, $\hat{u} \in C^2$, $A_\mu \in C^1$; Lipschitz boundaries $\partial\mathcal{U}_i, \partial\mathcal{U}_{ij}$; outward unit normal $\hat{n}_\mu$; $\sup_\tau \Vert J_E^\mu\Vert_{C^1} < \infty$ in coordinate components (compatible with divergent boundary flux, since $\sqrt{\vert g\vert}$ grows like $e^{nH_0\tau}$ (Branch I)). Timelike test trajectories satisfy $g_{\mu\nu}v^\mu v^\nu < 1$.

Added in r4:
* **Topology and cover:** $\mathcal{M}$ connected; $N_{\mathrm{nodes}} \ge 2$; overlap pairs $\langle i,j \rangle$ have $i \neq j$ (so $\mathcal{K}_0 \neq \emptyset$ and $\phi_{\mathrm{perc}}$ is defined).
* **Regularity:** $\mathcal{F} \in C^2(\mathcal{M})$; $\hat{g}_{\mu\nu} \in C^3(\mathcal{M})$, so that $\hat{h} \xrightarrow{C^2(\mathcal{M})} \hat{h}_\infty$ ($O_3$ Eq. 3); $\Phi^{(j)} \in C^4(\mathcal{M})$ and $\eta^\lambda_{i\to j} \in C^2(\mathcal{M})$ on all of $\mathcal{M}$, so $S^{(ij)}_{\mu\nu}$ is defined on $\partial\mathcal{U}_{ij}$; $\mathbf{J}^{\mathrm{harm}}_{\mathcal{M}} \in \Omega^1(\mathcal{M}) \cap C^2(\bar{\mathcal{M}})$.
* **Operators:** $\rho_{\mathrm{total}}(\tau)$ is a positive trace-class operator on $L^2(\mathcal{M}, d\mathrm{vol}_g)$.
* **Asymptotics:** For every $i$, $e^{-2H_0\tau}g^{(i)}_{\mu\nu} \xrightarrow{C^2(\mathcal{U}_i)} G^{(i)}_{\infty,\mu\nu} \succ 0$ and $\frac{1}{2}(g^{(i)})^{\mu\alpha}\partial_\tau g^{(i)}_{\alpha\nu} \xrightarrow{C^2(\mathcal{U}_i)} H_0\delta^\mu_\nu$, with common $H_0 > 0$ (Branch I; Decision 6 extends this to $H_0 \ge 0$, with $H_0 = 0$ in Branch II). Derived: $e^{-2H_0\tau}g_{\mu\nu} \xrightarrow{C^2(\mathcal{M})} G_{\infty,\mu\nu} \succ 0$.
* **Coupling:** $M^{(ij)}(\mathbf{x}) \neq 0$ for all $\mathbf{x} \in \bar{\mathcal{U}}_{ij}$; $\eta^\lambda_{[i\to j]} \not\equiv 0$ on $\mathcal{U}_{ij}$ for $\langle i,j \rangle \in \mathcal{K}$.
* **Notation:** The directed boundary element is $d\Sigma_\mu \equiv \hat{n}_\mu\,dA$ (formerly $dA_\mu$), so that it is not confused with the gauge connection $A_\mu$.

Clarified in r6:
* **Conformal factor:** $\Omega(\tau,\mathbf{x}) > 0$ is stated explicitly ($O_2$).
* **Harmonic current:** $\mathbf{J}^{\mathrm{harm}}_{\mathcal{M}}(\tau)$ is defined slice-wise on $\Sigma_\tau$ with the Hodge operators of $g_{\mu\nu}(\tau)$ ($O_5$).
* **Functional derivatives:** $\delta\Psi/\delta g_{\mu\nu}(\mathbf{x})$ and $\delta\Psi/\delta\mathcal{H}(\mathbf{x})$ are taken with respect to the coordinate measure $d^n x$, so both are weight-1 densities ($O_\Omega$).
* **Macroscopic free energy:** $\hat{\mathcal{F}}_{\mathrm{macro}} = \sum_i \hat{\mathcal{F}}_i$ sums the single-node weights $\psi_i$ only; the overlap weights $\psi_{ij}$ carry no free-energy section ($O_7$).

Clarified in r5:
* **Subsystem densities:** $Q_i$ is an independent object on $\mathcal{U}_i$ that *need not* coincide with the restriction of the global $Q$; nothing forbids equality (the §5 model has $\mathcal{U}_1 = \mathcal{M}$ and $Q_1 = Q$).

Added in r7/r10 (Decision 6):
* **Branches:** every configuration is in Branch I ($H_0 > 0$, the r6 hypotheses) or Branch II ($H_0 = 0$, $\int_{\tau_0}^\infty\langle\theta\rangle_{\mathcal{M}}\,d\tau < \infty$, $\langle\Theta_E\rangle_{\mathcal{M}} \to \Theta_\infty > 0$). The homothety hypotheses of $O_5$ Eq. [4] are stated for common $H_0 \ge 0$.
* **Throughput:** $\Theta_E = \dot{s}_{\mathrm{prod}}/s_0 > 0$ everywhere on $\mathcal{M}$ at every $\tau$, in both branches.
* **Branch declaration:** every evaluation declares its branch before the test (closure condition (v)).
* **Constitutive closure:** $f^\mu_{\mathrm{drive}}$, $\mathfrak{K}^{\alpha\beta} \succ 0$, and $\mathcal{R}_{\mathcal{F}} \ge 0$ take their defaults unless declared a priori from named constitutive laws with independently measured parameters.

---

## 4. Master Standardized Symbol Table (`foundational-manifold-2026-10-20-r7.json`)

| Symbol | Category | Meaning & Coordinate Introduced |
| :--- | :--- | :--- |
| $\mathcal{M}, \; \partial\mathcal{M}, \; \Sigma_\tau$ | Geometry | Compact, connected $n$-dimensional spatial manifold ($n \ge 3$), smooth boundary, and constant-$\tau$ hypersurface ($O_0$). |
| $\tau, \; N, \; \beta^\mu$ | ADM Foliation | Foliation time (proper time of normal observers at $N=1, \beta^\mu=0$), lapse function, and shift vector ($O_0$). |
| $g_{\mu\nu} \equiv g_{\mu\nu}^{\mathrm{macro}}$ | Metric | Global Riemannian metric on $\Sigma_\tau$, glued in $O_5$ from local subsystem metrics $g_{\mu\nu}^{(i)}$ and overlap geometric means $g_{\mu\nu}^{(ij)} = (g^{(i)} \# g^{(j)})_{\mu\nu}$. |
| $G^{(i)}_{\infty,\mu\nu}, \; G_{\infty,\mu\nu}$ | Asymptotics | $C^2$ limits of $e^{-2H_0\tau}g^{(i)}_{\mu\nu}$ (hypothesis) and of $e^{-2H_0\tau}g_{\mu\nu}$ (derived), both positive-definite ($O_5$ Eq. 4). Not to be confused with $\tilde{g} = \Omega^{-2}g \to \hat{g}_\infty$. |
| $\Omega, \; \hat{g}_{\mu\nu}, \; \hat{g}_{\infty,\mu\nu}$ | Weyl Split | Conformal factor (scalar density of weight $1/n$ in the fixed reference chart), unit-determinant reference metric ($\det\hat{g}=1$), and absorbed asymptotic reference metric ($O_2, O_3$). |
| $h_{\mu\nu}, \; \hat{h}^\alpha_{\;\nu}, \; \sigma^\mu_{\;\nu}$ | Shear | Symmetric shear perturbation, $\hat{g}$-traceless endomorphism ($\hat{g}^{\alpha\beta}h_{\beta\nu}$), and mixed trace-free extrinsic shear tensor ($O_2, O_3$). |
| $K_{\mu\nu}, \; \theta, \; \mathcal{D}^\mu_{\;\nu}$ | Extrinsic | ADM extrinsic curvature tensor, normal expansion scalar ($\theta \equiv -N K = \nabla_\mu J_{\mathrm{geom}}^\mu \ge 0$; $> 0$ in Branch I), and deformation endomorphism ($\mathcal{D}^\mu_{\;\nu} \equiv -N K^\mu_{\;\nu}$) ($O_0, O_2, O_6$). |
| $J_E^\mu, \; J_W^\alpha, \; u_{\mathrm{exp}}^\mu$ | Fluxes | Throughput current ($O_0$, $O_1$; equal to $J_{\mathrm{geom}}^\mu$ in Branch I, fixed as $J_W^\mu/p_0$ in Branch II), free-energy transport current $-\mathfrak{K}^{\alpha\beta}\nabla_\beta\mathcal{F}$ ($O_4$), and intrinsic metric expansion velocity field ($O_7$). |
| $J_{\mathrm{geom}}^\mu$ | Fluxes (r7) | Expansion current: $\nabla_\mu J_{\mathrm{geom}}^\mu = \theta$, $\oint J_{\mathrm{geom}}^\mu\,d\Sigma_\mu = dV_{\mathcal{M}}/d\tau$; in Branch I, $J_{\mathrm{geom}} \equiv J_{\mathrm{ambient}}\vert_{\mathcal{M}}$ pointwise, as in r6 ($O_0$). |
| $J_{\mathrm{ambient}}^\mu$ | Fluxes (r6) | Ambient exogenous flux of the field, restricted to $\mathcal{M}$ to fix $J_{\mathrm{geom}}$ pointwise in Branch I ($O_0$). |
| $u^2$ | Kinematics (r7) | $g_{\mu\nu}v^\mu v^\nu$, the squared speed of a test trajectory ($< 1$, timelike) ($O_2$). |
| $\Theta_E, \; \Theta_{\mathrm{tot}}, \; \tau_\Theta, \; \langle\cdot\rangle_{\mathcal{M}}$ | Throughput (r7) | Throughput rate $\dot{s}_{\mathrm{prod}}/s_0 > 0$, total rate $\sqrt{\theta^2 + \Theta_E^2}$, emergent clock $\int\langle\Theta_{\mathrm{tot}}\rangle\,d\tau$, and volume average ($O_0$). |
| $\mathfrak{K}^{\alpha\beta}, \; \mathcal{R}_{\mathcal{F}}, \; f^\mu_{\mathrm{drive}}, \; a^\mu_{\mathrm{d}}$ | Constitutive (r7) | Declared transport tensor ($\succ 0$, $C^1$; default $D_{\mathcal{F}}g^{\alpha\beta}$), interior sink ($\ge 0$, $C^0$; default $0$) ($O_4$), cone-preserving drive $(1-u^2)(a_{\mathrm{d}} - (a_{\mathrm{d}}\cdot v)v)$ with declared drive acceleration $a_{\mathrm{d}}$ (default $0$) ($O_2$). |
| $s_0$ | Entropy density (r6, r7) | Positive constant: the $O_\Omega$ Eq. [0] saturation density (information per unit volume), also used in r7 to normalize $\Theta_E = \dot{s}_{\mathrm{prod}}/s_0$; finite-$\tau$ values of $\Theta_E$, $\tau_\Theta$, and $\chi_E$ depend on it, while the sign and limit statements about $\Theta_E$, $\tau_\Theta$, and $\chi_E$ (positivity, monotonicity, $\chi_E \to 1$) are invariant under rescaling $s_0$; the $O_\Omega$ Eq. [0] limit itself fixes $s_0$. |
| $\mathfrak{K}^{\alpha\beta}$ notation | (r7) | The transport tensor is written $\mathfrak{K}$; in the spine, $K$, $K_{\mu\nu}$, and $K^\mu_{\;\nu}$ denote extrinsic curvature (§5.9 uses $K$ for Gaussian curvature). |
| $J_W^{\mathrm{meas}}$ | Closure (r7) | Free-energy flux measured directly, within the test window, across a declared surface, by a method independent of the declared $\mathfrak{K}$; compared with $-\mathfrak{K}\nabla\mathcal{F}$ under a pre-declared tolerance ($O_1$, $O_4$ closure). |
| $\dot{W}_{\mathrm{diss}}, \; \dot{W}_{\mathrm{tot}}$ | Power (r7) | Dissipative power $\int(-J_E\cdot\nabla\mathcal{F})\sqrt{\vert g\vert}\,d^nx > 0$ and total power $\dot{W}_{\mathrm{ext}} + \dot{W}_{\mathrm{diss}} > 0$ ($O_1$). |
| $\chi_E, \; V_\infty, \; \Theta_\infty$ | Branch II (r7) | Throughput-normalized anisotropy index, finite asymptotic volume, and asymptotic throughput rate ($O_7$, $O_0$, $O_\Omega$). |
| $d\Sigma_\mu, \; \hat{n}_\mu$ | Boundary | Directed boundary element $d\Sigma_\mu \equiv \hat{n}_\mu\,dA$ and outward unit normal ($O_0, O_1, O_4, O_7$). |
| $\mathbf{J}_{\mathcal{M}}^{\mathrm{harm}}$ | Harmonic Current | Harmonic 1-form, $\Omega^1(\mathcal{M}) \cap C^2(\bar{\mathcal{M}})$, with $d\mathbf{J} = d^\dagger\mathbf{J} = 0$ and absolute boundary conditions; it exists non-trivially because $H^1_{\mathrm{dR}}(\mathcal{M}) \neq 0$ ($O_5$). |
| $\mathcal{H}, \; \mathcal{H}_{\mathrm{sol}}$ | Hysteresis | Structural hysteresis scalar field ($\partial_\tau \mathcal{H} = J_E^\mu \nabla_\mu q$, strongly convex $\nabla_\alpha\nabla_\beta\mathcal{H} \succ 0$) and ultralocal stationary solution ($O_0, O_3, O_7, O_\Omega$). |
| $Q, \; P, \; q, \; v_0$ | Information | Global generative density ($Q > 0$, obtained from the spectrally gated state $\rho_{\mathrm{local}}$ of the positive trace-class operator $\rho_{\mathrm{total}}$ on $L^2(\mathcal{M}, d\mathrm{vol}_g)$ via the low-pass projector $\hat{\mathcal{P}}_{\Lambda_{\mathrm{gate}}}$), normalized reference prior density ($Q \ll P$), dimensionless surprisal $q \equiv -\ln(v_0 Q)$, and elementary reference volume ($O_0, O_4$). |
| $Q_i, \; Q_{ij}, \; Q_i^{\vert ij}$ | Subsystem Info | Subsystem density on $\mathcal{U}_i$, pairwise joint density on $\mathcal{U}_i \times \mathcal{U}_j$, and normalized overlap-conditional density on $\mathcal{U}_{ij}$ ($O_6$). |
| $\mathcal{F}, \; D_{\mathcal{F}}, \; \beta_{\mathrm{th}}, \; p_0$ | Thermodynamics | Scalar free-energy density, constant diffusivity, inverse temperature, and reference pressure $p_0 \equiv (\beta_{\mathrm{th}}v_0)^{-1}$ ($O_1, O_4$). |
| $\dot{W}_{\mathrm{ext}}, \; \dot{W}_{\mathrm{var}}, \; \dot{s}_{\mathrm{prod}}$ | Power & Entropy | Mechanical expansion power ($O_1$), variational realignment power ($O_4$), and local entropy production rate ($O_1$). |
| $\Phi, \; \Pi_{\mu\nu}, \; \hat{\Pi}_{\mu\nu}, \; f_\mu^{\mathrm{top}}$ | Potential | Environmental scalar potential, covariant Hessian ($\nabla_\mu\nabla_\nu\Phi$), trace-free Hessian, and topological restoring force ($O_2, O_3, O_4$). |
| $\eta^\lambda, \; \xi_\nu, \; T_{\mu\nu}^{\mathrm{mat}}, \; \kappa_G$ | Boundary Stress | Boundary control vector field, precision-weighted 1-form ($\hat{\Pi}_{\nu\lambda}\eta^\lambda$), conserved stress-energy tensor, and gravitational coupling ($O_2, O_4$). |
| $\mathbb{L}_{\mathrm{Ein}}[\sigma]_{\mu\nu}, \; \hat{\mathbb{L}}_{\mathrm{stat}}(\mathbf{x})$ | Operators | Linearized Einstein operator on trace-free perturbations ($O_2, O_4$) and pointwise first-order stationary flow generator ($O_\Omega$). |
| $(J_{i\to j})_\nu, \; (J_{[i\to j]})_\nu, \; F_{\mu\alpha}^{(i\to j)}$ | Edge Coupling | Partner-directed coupling 1-form, precision-symmetrized phase-lead 1-form, and exterior-curvature 2-form ($O_6$). |
| $M_{\mu\nu}^{(ij)}, \; S_{\mu\nu}^{(ij)}, \; \gamma_M, \; \ell_F^2$ | Edge Tensors | Trace-free conformal-quadratic deformation operator, total trace-free coupling tensor, and coupling constants ($O_6$). |
| $\mathcal{P}_{\mathrm{gauge}}, \; G_{\mathrm{gauge}}, \; A_\mu, \; F_{\mu\nu}^{\mathrm{YM}}$ | Gauge Bundle | Principal bundle over $\mathcal{M}$ with compact group $G_{\mathrm{gauge}}$, Hermitian Lie algebra generators $\{\hat{T}_a\}$, bounded $C^1$ connection $A_\mu$ with constant coupling $g_{\mathrm{YM}} \neq 0$, and curvature ($O_7$). |
| $\chi, \; \hat{\chi}, \; \hat{\mathcal{E}}_\mu, \; \hat{\mathcal{F}}_i$ | Adjoint Sections | $C^2$, kink-free anisotropy scalar ($n\,\mathrm{Tr}(\mathcal{D}^2)/(\mathrm{Tr}\,\mathcal{D})^2$), adjoint anisotropy section ($\chi\,\hat{u}$ in Branch I, $\chi_E\,\hat{u}$ in Branch II; $\Vert\hat{u}\Vert_{\mathfrak{g}} = 1$), spatial impedance gradient ($D_\mu\hat{\chi}$), and adjoint free energy ($\psi_i\,\mathcal{F}\,\hat{e}_i$, $\Vert\hat{e}_i\Vert_{\mathfrak{g}} = 1$) ($O_7$). |
| $\hat{\rho}_g, \; \hat{\rho}_{\mathcal{H}}$ | Endomorphisms | Unit-trace type-$(1,1)$ density endomorphisms normalized via $\hat{g}_\infty^{\mu\alpha}$ ($O_7$). |
| $\mathcal{K}_0, \; \mathcal{K}, \; \phi_{\mathrm{perc}}, \; \phi_c$ | Graph | Geometric overlap graph (pairs $i \neq j$), actively coupled subgraph ($\eta_{[i\to j]} \not\equiv 0$), active-edge fraction $\vert\mathcal{K}\vert/\vert\mathcal{K}_0\vert$, and critical threshold $\phi_c \in (0,1)$ ($O_5$). |
| $\rho_{\mathrm{top}}^{(ij)}, \; \mathbf{C}_{\mathrm{top}}^{(ij)}$ | Overlap Invariants | Topological density and parallel-transported correlation tensor of overlap $\mathcal{U}_{ij}$ ($O_5$). |
| $k_{\mathcal{I}}$ | Coupling | Positive constant converting the coupling-tensor boundary flux into mutual-information growth rate ($O_6$). |
| $\mathcal{A}_{\mathcal{M}}$ | Action | Global surprisal action pairing the control field $\eta^\mu$ with $\nabla_\mu q$ ($O_7$). |
| $\Psi[g_{\mu\nu}, \mathcal{H}]$ | Functional | Smooth functional on $\mathrm{Met}(\mathcal{M}) \times C^\infty(\mathcal{M})$, invariant under $\hat{\mathbb{L}}_{\mathrm{stat}}$ on the stationary graph locus ($O_\Omega$). |

---

## 5. Joint Satisfiability: Explicit Two-Subsystem Model on a Flat Annular Domain

This section exhibits one configuration with $n = 3$ and $N_{\mathrm{nodes}} = 2$ that satisfies every equation and hypothesis of `foundational-manifold-2026-10-20-r6.json` simultaneously, so the hypothesis set is not contradictory. Everything is written in the fixed chart $\mathbf{x} \in \mathbb{R}^3$, with $\varrho = \sqrt{(x^1)^2 + (x^2)^2}$, azimuth $\varphi$, and $\vert\mathbf{x}\vert$ the Euclidean norm.

### 5.1 Domain and cover
* **Domain.** $\mathcal{M}$ is the hollow cylinder $\{R_1 \le \varrho \le R_2, \; 0 \le x^3 \le L\}$ ($0 < R_1 < R_2$), with its four circular rim edges rounded axisymmetrically so that $\partial\mathcal{M}$ is smooth, as $O_0$ requires; the unrounded cylinder has corners.
* **Topology.** $\mathcal{M}$ is compact and connected with $H^1_{\mathrm{dR}}(\mathcal{M}) \cong \mathbb{R}$. It avoids the $x^3$-axis, so $\vert\mathbf{x}\vert \ge R_1 > 0$ and $\varphi$ is smooth on $\bar{\mathcal{M}}$.
* **Cover.** $\mathcal{U}_1 = \mathcal{M}$. $\mathcal{U}_2 = E$ is an open oblate ellipsoid with semi-axes $b_1 < b_2 = b_3$, its short axis along $x^1$, contained in the interior of $\mathcal{M}$ (for example centred at $((R_1+R_2)/2, 0, L/2)$ with $b_1, b_2$ small). Then $\mathcal{U}_{12} = E$ is geodesically convex with smooth boundary.
* **Graph.** $\mathcal{K}_0 = \mathcal{K} = \{\langle 1,2 \rangle\}$, so $\phi_{\mathrm{perc}} = 1 > \phi_c$.
* **Partition of unity.** $\psi_{12} \in C^\infty_c(E)$ with $0 \le \psi_{12} \le 1$, $\psi_2 = 0$, and $\psi_1 = 1 - \psi_{12}$.

### 5.2 Metric and kinematics
* **Metrics.** $g^{(1)}_{\mu\nu} = g^{(2)}_{\mu\nu} = e^{2H_0\tau}\delta_{\mu\nu}$. Hence $g^{(12)} = g^{(1)} \# g^{(2)} = g^{(1)}$, and the glued metric is $g_{\mu\nu} = e^{2H_0\tau}\delta_{\mu\nu}$.
* **Weyl split.** $\Omega = e^{H_0\tau}$, $\hat{g} = \delta$, $\hat{h} = \hat{h}_\infty = 0$, $\hat{g}_\infty = \tilde{g} = \delta$, and $G^{(i)}_\infty = G_\infty = \delta$.
* **Expansion and shear.** $\theta = 3H_0$ and $\sigma^\mu_{\;\nu} = 0$, so the shear law holds for any $\gamma_\sigma > 0$. $\mathcal{D}^\mu_{\;\nu} = H_0\delta^\mu_\nu$, so $\lambda_{\min}(\mathcal{D}) = H_0 > 0$.
* **Curvature.** $\Gamma^\lambda_{\mu\nu} = 0$ and the Riemann tensor vanishes.
* **Asymptotics.** $O_5$ Eq. 4 and $O_\Omega$ Eq. 1 hold exactly, not just in the limit.

### 5.3 Flux, free energy, potential, stress
* **Exogenous flux.** $J_E^\mu = H_0 x^\mu$. Then $\nabla_\mu J_E^\mu = 3H_0 = \theta$, $\sup_\tau \Vert J_E\Vert_{C^1} < \infty$, and $\oint_{\partial\mathcal{M}} J_E^\mu \, d\Sigma_\mu = 3H_0 V_{\mathcal{M}} \to \infty$.
* **Free energy.** $\mathcal{F} = c_{\mathcal{F}}\,e^{-3H_0\tau}/\vert\mathbf{x}\vert$ with $c_{\mathcal{F}} > 0$, which is $C^2$ on $\mathcal{M}$.
  * Balance law: $\partial_\tau\mathcal{F} + \theta\mathcal{F} = 0 = D_{\mathcal{F}}\nabla^2\mathcal{F}$, since $\Delta\vert\mathbf{x}\vert^{-1} = 0$ away from the origin.
  * Gradient condition: $J_E^\mu\nabla_\mu\mathcal{F} = -H_0 c_{\mathcal{F}}\,e^{-3H_0\tau}/\vert\mathbf{x}\vert < 0$, so $\nabla\mathcal{F} \neq 0$ and $\dot{s}_{\mathrm{prod}} > 0$.
* **Global potential and stress.** $\Phi = \frac{c_\Phi}{2}\vert\mathbf{x}\vert^2$ gives $\Pi_{\mu\nu} = c_\Phi\delta_{\mu\nu}$, so $\hat{\Pi}_{\mu\nu} = 0$ and $\xi_\nu = 0$ for any $C^2$ field $\eta^\lambda$ (take $\eta^\lambda = 0$). Then:
  * $T^{\mathrm{mat}}_{\mu\nu} = 0 = G_{\mu\nu}$, $R = \kappa_G\nabla_\alpha\xi^\alpha = 0$, and $\nabla^\mu T_{\mu\nu} = 0$.
  * The $\tau$-compatibility law and its elliptic trace hold with both sides zero.

### 5.4 Global information and the asymptotic generator
* **Generative density.** $\rho_{\mathrm{total}}(\tau) = \vert\phi_0\rangle\langle\phi_0\vert$, where $\phi_0 = \mathrm{Vol}_g(\mathcal{M})^{-1/2}$ is the constant Neumann mode. Its eigenvalue is 0, so it passes any gate $\Lambda_{\mathrm{gate}} \ge 0$. This gives $Q = e^{-3H_0\tau}/\mathrm{Vol}_\delta(\mathcal{M}) > 0$, normalized, with $q$ spatially constant, so $J_E^\mu\nabla_\mu q = 0$.
* **Reference prior.** $P = Q\,(1 + \epsilon(\tau)u)$, with $\int_{\mathcal{M}} u\,Q\sqrt{\vert g\vert} \, d^3x = 0$ (here $Q\sqrt{\vert g\vert}$ is spatially constant, so this is $\int_{\mathcal{M}} u \, d^3x = 0$; every later reuse of this prior, in §5.10, §5.11 and §5.13, uses the weighted condition, which is what normalization $\int P\sqrt{\vert g\vert} = 1$ requires; where $Q\sqrt{\vert g\vert}$ varies in $\tau$ the condition must hold at every $\tau$. In §5.10 (flat, homothetic), $Q\sqrt{\vert g\vert} = (1-\varepsilon_q)/\bar{V} + \varepsilon_q\bar{\phi}_1^2$ with a fixed $\bar{\phi}_1$, so a $\tau$-independent $u$ needs the two moment conditions $\int u = 0$ and $\int u\,\bar{\phi}_1^2 = 0$. In §5.11, $\sqrt{\vert g\vert} = e^{3H_0\tau}z^{\sqrt{2}}$ and the shear changes the shape of the first Neumann mode, so the conditions are $\int u\,z^{\sqrt{2}}\,d^3x = 0$ and $\int u\,\bar{\phi}_1(\tau)^2z^{\sqrt{2}}\,d^3x = 0$ for every $\tau$; one construction satisfying all of them is an axisymmetric ($m = 0$) mode $\phi_1$, which §5.11 permits, with $u = b(\varrho, z)\cos\varphi$ and $\vert b\vert < 1$, since the azimuthal integral of $\cos\varphi$ vanishes against every axisymmetric weight), $\vert u \vert < 1$, $u \not\equiv 0$, and $\epsilon(\tau) \in (0,1)$ decreasing to $0$. Then $Q \ll P$, $D_{\mathrm{KL}}(Q \parallel P) > 0$ (so $\dot{W}_{\mathrm{var}} > 0$), and $V_Q/V_P \to 1$.
* **Hysteresis.** $\mathcal{H} = \frac{c_{\mathcal{H}}}{2}\vert\mathbf{x}\vert^2$ with $c_{\mathcal{H}} > 0$.
  * $\partial_\tau\mathcal{H} = 0 = J_E^\mu\nabla_\mu q$.
  * $\nabla_\alpha\nabla_\beta\mathcal{H} = c_{\mathcal{H}}\delta_{\alpha\beta} \succ 0$.
  * $\hat{\rho}_{\mathcal{H}} = \hat{\rho}_g = \frac{1}{3}\delta^\mu_\nu$, so $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) = 0$.
* **Generator ($O_\Omega$).** $\mathcal{H}_{\mathrm{sol}}(g,\mathbf{x}) = \frac{c_{\mathcal{H}}}{2}\vert\mathbf{x}\vert^2$ is ultralocal with $\partial\mathcal{H}_{\mathrm{sol}}/\partial g_{\mu\nu} = 0$, which equals the right-hand side of $O_\Omega$ Eq. 2 because $J_E^\lambda\nabla_\lambda q = 0$. Take $\Psi[g,\mathcal{H}] = \int_{\mathcal{M}} \mathcal{H} \, d^3x$. Then $\delta\Psi/\delta g = 0$, $\delta\Psi/\delta\mathcal{H} = 1 \neq 0$, the locus condition holds, and $\hat{\mathbb{L}}_{\mathrm{stat}}\Psi = 0$.

### 5.5 Relational edge
* **Local potentials.** $\Phi^{(1)} = \Phi^{(2)} = \frac{1}{2}\left((x^1)^2 - (x^2)^2\right)$ on all of $\mathcal{M}$. Then $\hat{\Pi}^{(j)}_{\mu\nu} = \mathrm{diag}(1,-1,0)$, which is already $g$-trace-free.
* **Coupling fields.** $\eta^\lambda_{1\to 2} = -\eta^\lambda_{2\to 1} = a(\tau)\,\delta^\lambda_1$ with $a(\tau) = a_0 e^{3H_0\tau/2}$ and $a_0 \neq 0$. These are spatially constant, hence $C^2$ on $\mathcal{M}$.
* **Derived 1-forms.** $\eta_{[1\to 2]} = a\,\partial_1 \not\equiv 0$. $J_{1\to 2} + J_{2\to 1} = 0$, so the first term of $M^{(12)}$ vanishes. $J_{[1\to 2]} = a\,dx^1$, and $F^{(1\to 2)} = F^{(2\to 1)} = 0$.
* **Coupling tensor.** $S^{(12)}_{\mu\nu} = M^{(12)}_{\mu\nu} = \gamma_M a^2\left(\delta_{\mu 1}\delta_{\nu 1} - \frac{1}{3}\delta_{\mu\nu}\right)$.
  * It is trace-free and nonzero at every point of $\bar{E}$.
  * Its mixed eigenvalues are $e^{-2H_0\tau}\gamma_M a^2\,(\tfrac{2}{3}, -\tfrac{1}{3}, -\tfrac{1}{3})$, so $m_+ > 0 > m_-$ with $m_+ \neq -m_-$.
* **Boundary flux.** With $\hat{n}^\mu = e^{-H_0\tau}\nu^\mu$ and $dA = e^{2H_0\tau}dA_\delta$:
  * $\oint_{\partial E} S^{(12)}_{\mu\nu}\hat{n}^\mu\hat{n}^\nu \, dA = \gamma_M a(\tau)^2\,C_E$, where $C_E \equiv \oint_{\partial E}(\nu_1^2 - \tfrac{1}{3}) \, dA_\delta$.
  * $C_E = 0$ when $E$ is a ball, because a constant trace-free tensor has zero flux through a sphere. That would force $d\mathcal{I}/d\tau = 0$, which is why $\mathcal{U}_{12}$ must not be a ball.
  * For an oblate $E$ with short axis along $x^1$, $C_E > 0$; numerically, $C_E \approx 3.64$ for semi-axes $(0.2, 1, 1)$.
* **Subsystem densities.** $Q_1 = 1/\mathrm{Vol}_g(\mathcal{M})$ and $Q_2 = 1/\mathrm{Vol}_g(E)$ (uniform). Then $Q_1^{\vert 12} = Q_2^{\vert 12}$ (uniform on $E$), so $D_{\mathrm{KL}}(Q_1^{\vert 12} \parallel Q_2^{\vert 12}) = 0$ for all $\tau$.
* **Required mutual information.** $\mathcal{I}(\tau) = k_{\mathcal{I}}\gamma_M a_0^2 C_E\,(e^{3H_0\tau} - e^{3H_0\tau_0})/(3H_0)$, so $d\mathcal{I}/d\tau = k_{\mathcal{I}}\gamma_M a_0^2 C_E\,e^{3H_0\tau} > 0$.
* **Joint density (sketch).** Partition $\mathcal{M}$ and $E$ into $m$ cells each, of equal relative volume. Set $Q_{12} = (1-w)\,Q_1 \otimes Q_2 + w\,m\,(Q_1 \otimes Q_2)\,\mathbf{1}_{\text{matched cells}}$.
  * For every $w \in [0,1]$ this has exact marginals $Q_1, Q_2$ and satisfies $Q_{12} \ll Q_1 \otimes Q_2$.
  * Its mutual information increases continuously from $0$ to $\ln m$ as $w$ goes from 0 to 1.
  * Interpolating between nested refinements $m \to km$ in the same way extends the range to $[0, \infty)$, so a choice of $(m, w)$ as a function of $\tau$ realizes the prescribed $\mathcal{I}(\tau)$. The densities are piecewise constant, which the specification permits (no regularity is imposed on $Q_{ij}$).
* **Saturation and volume share.** Setting $s_0 = k_{\mathcal{I}}\gamma_M a_0^2 C_E / (3H_0\,\mathrm{Vol}_\delta(\mathcal{M}))$ gives $\mathcal{I}/(s_0 V_{\mathcal{M}}) \to 1$. Also $V_{1\cup 2}/V_{\mathcal{M}} = 1 \in (0,1]$.

### 5.6 Harmonic current and gauge sector
* **Harmonic current.** $\mathbf{J}^{\mathrm{harm}}_{\mathcal{M}} = c_{\mathrm{harm}}\,d\varphi$ with $c_{\mathrm{harm}} \neq 0$.
  * It is smooth on $\bar{\mathcal{M}}$ and closed.
  * $d^\dagger\mathbf{J} = 0$ because $\Delta\varphi = 0$; the conformal factor is spatially constant, so this holds for every $\tau$.
  * On an axisymmetric boundary $\hat{n}$ lies in the meridian plane, so $\iota_n\mathbf{J} = 0$ and $\iota_n d\mathbf{J} = 0$ (absolute boundary conditions).
  * It represents the generator of $H^1_{\mathrm{dR}}(\mathcal{M})$.
* **Gauge sector.** $G_{\mathrm{gauge}} = SU(2)$ on the trivial bundle, with $A_\mu = 0$, $g_{\mathrm{YM}} = 1$, and constant unit $\hat{u}, \hat{e}_i$.
  * $\chi = 1$ (since $\sigma = 0$), so $\hat{\chi} = \hat{u}$, $\hat{\mathcal{E}}_\mu = 0$, and $[F^{\mathrm{YM}}_{\mu\nu}, \hat{\chi}] = 0$.
  * Take $u_{\mathrm{exp}} = J_E$. Then $\mathcal{L}_{\mathbf{J}_E}(\hat{h} - \hat{h}_\infty) = 0$ and $\mathcal{A}_{\mathcal{M}} = 0$.

### 5.7 Differences from the transmitted model, and limits
* **Rounded edges.** Added so that $\partial\mathcal{M}$ is smooth.
* **Hysteresis term dropped.** The term $\frac{c_q}{3H_0}\ln\sqrt{\vert g\vert}$ is omitted from $\mathcal{H}$ (i.e., $c_q = 0$).
  * With $c_q \neq 0$ the model would need $J_E^\mu\nabla_\mu q = c_q$, which forces $Q \propto \vert\mathbf{x}\vert^{-c_q/H_0}$ times a degree-0 angular factor.
  * $O_4$ requires $Q = \langle\mathbf{x}\vert\rho_{\mathrm{local}}\vert\mathbf{x}\rangle$ with $\rho_{\mathrm{local}}$ in the range of a finite-rank Neumann low-pass projector. It has not been shown that such a $Q$ has this form.
  * With $c_q = 0$, the $O_\Omega$ generator equivalence holds with both sides zero. It is therefore satisfied but only trivially exercised.
* **$\hat{\Pi}^{(j)} \neq 0$ does not by itself imply $M^{(12)} \neq 0$.** Here $M^{(12)} \neq 0$ because $J_{[1\to 2]} = \hat{\Pi}\,\eta_{[1\to 2]} \neq 0$ at every point for the chosen $\eta$.
* **The overlap is an oblate ellipsoid, not a ball.** See the flux discussion in §5.5.
* **Orientation matters, not just non-sphericity.** $C_E$ changes sign with shape: a prolate ellipsoid with its long axis along $x^1$ (semi-axes $(2,1,1)$) gives $C_E \approx -4.19 < 0$, which would violate $d\mathcal{I}/d\tau > 0$. The overlap must be flattened along the direction of $J_{[1\to 2]}$.
* **Data added to complete the model:** $\mathcal{F}$, $\rho_{\mathrm{total}}$, $Q$, $P$, the cover and partition of unity, $\eta_{i\to j}$ with growth rate $a(\tau)$, $Q_{12}$, $s_0$, $\Psi$, and the gauge data.
* **Scope.** The model establishes consistency of the hypothesis set, not genericity. Constructing $Q_{12}(\tau)$ smoothly in $\tau$ is sketched, not written out.
* **Independent re-check (r5).** Every equation and hypothesis of the r5 JSON was re-derived against this model. Numerical checks confirm $C_E \approx 3.642$ for semi-axes $(0.2,1,1)$ and $C_E \approx 0$ for a sphere. For the block coupling, the marginals are exact, and the mutual information increases monotonically from $0$ to $\ln m$. Under nested refinement it covers $[\ln m, \ln km]$: coarse-graining to the level-$m$ cells gives exactly $\ln m$, so data processing bounds it below. The model is deliberately degenerate in places: $\hat{\Pi} = 0$ globally (so $T^{\mathrm{mat}} = 0$ and $\kappa_G$ is unexercised), $\sigma \equiv 0$, $A_\mu = 0$, $J_E^\mu\nabla_\mu q = 0$, and $D_{\mathrm{KL}}(Q_1^{\vert 12} \parallel Q_2^{\vert 12}) \equiv 0$. §5.8 switches most of those sectors on; two remain trivial, for reasons stated there.

### 5.8 Non-degenerate active-sector extension (r6)
This extension keeps the domain, cover, partition of unity, $J_E^\mu = H_0 x^\mu$, $\rho_{\mathrm{total}}$, $Q$, $P$, and $\Psi$ of §5.1–5.6, and replaces the rest as listed. It switches on shear, $\chi > 1$, $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) > 0$, global $\hat{\Pi}$, $\eta$, $\xi$, a non-flat gauge connection with $\hat{\mathcal{E}}_\mu \not\equiv 0$, and a non-zero overlap divergence. All of these decay to their asymptotic values. Every claim below was checked symbolically or numerically for r6.

**Constants.** $H_0 > 0$; a shear amplitude $s_\sigma$ with $0 < s_\sigma < H_0/2$ (written $s_0$ in the transmitted model; renamed because $s_0$ is the information-saturation constant of $O_\Omega$); $\gamma_\sigma > 0$. Write $a(\tau) \equiv (2 s_\sigma/\gamma_\sigma)(1 - e^{-\gamma_\sigma(\tau-\tau_0)})$, which increases from $0$ to $a_\infty \equiv 2 s_\sigma/\gamma_\sigma$.

**Metric and shear.**
* **Metric (axisymmetric Bianchi I).** $g^{(1)} = g^{(2)} = g = e^{2H_0\tau}\,\mathrm{diag}(e^{a}, e^{a}, e^{-2a})$. Its Weyl split is $\hat{g} = \delta$, $\Omega = e^{H_0\tau}$, $\hat{h} = a(\tau)\,\mathrm{diag}(1,1,-2)$.
* **Asymptotic metrics.** $\hat{h}_\infty = a_\infty\,\mathrm{diag}(1,1,-2) \neq 0$, and $\hat{g}_\infty = G_\infty = G^{(i)}_\infty = \mathrm{diag}(e^{a_\infty}, e^{a_\infty}, e^{-2a_\infty})$, with $\det = 1$.
* **Flat slices.** The components are spatially constant, so $\Gamma = 0$ and the Riemann tensor vanishes on every slice. Hence $G_{\mu\nu} = 0$, $\mathbb{L}_{\mathrm{Ein}}[\sigma]_{\mu\nu} = 0$, and $\nabla\nabla\theta = 0$ for all $\tau$, even though the shear is non-zero.
* **Shear.** $\sigma^\mu_{\;\nu} = \tfrac{1}{2}\partial_\tau\hat{h} = s_\sigma e^{-\gamma_\sigma(\tau-\tau_0)}\,\mathrm{diag}(1,1,-2) \not\equiv 0$.
  * It obeys the $O_3$ damping law exactly.
  * $\theta = 3H_0$.
  * $\lambda_{\min}(\mathcal{D}) = H_0 - 2 s_\sigma e^{-\gamma_\sigma(\tau-\tau_0)} \ge H_0 - 2s_\sigma > 0$.
  * $\tfrac{1}{2}g^{-1}\partial_\tau g = H_0 I + \sigma \to H_0 I$, as $O_5$ Eq. 4 and $O_\Omega$ Eq. 1 require.
* **Anisotropy.** $\chi(\tau) = 1 + 2 s_\sigma^2 e^{-2\gamma_\sigma(\tau-\tau_0)}/H_0^2$, which is $> 1$ for finite $\tau$ and tends to $1$.

**Hysteresis and endomorphisms.**
* **Hysteresis.** $\mathcal{H} = \tfrac{c_{\mathcal{H}}}{2}\,\hat{g}_{\infty,\alpha\beta}x^\alpha x^\beta$ ($c_{\mathcal{H}} > 0$), so $\nabla\nabla\mathcal{H} = c_{\mathcal{H}}\hat{g}_\infty \succ 0$ and $\hat{\rho}_{\mathcal{H}} = \tfrac{1}{3}\delta$.
* **Metric endomorphism.** $\hat{\rho}_g = \mathrm{diag}(e^{a-a_\infty}, e^{a-a_\infty}, e^{-2(a-a_\infty)})/\mathrm{Tr}(\cdot)$, which differs from $\tfrac{1}{3}\delta$ at every finite $\tau$.
* **Relative entropy.** Therefore $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) > 0$, and it tends to $0$.
* **Consistency with $O_0$.** $\partial_\tau\mathcal{H} = 0 = J_E^\mu\nabla_\mu q$, since $q$ is spatially constant.

**Free energy (corrected).**
* **The §5.3 choice fails here.** $c_{\mathcal{F}}e^{-3H_0\tau}/\vert\mathbf{x}\vert$ is not harmonic for the anisotropic Laplacian $\nabla^2 = e^{-2H_0\tau}[e^{-a}(\partial_1^2 + \partial_2^2) + e^{2a}\partial_3^2]$.
* **So does the transmitted variant.** $\vert\mathbf{x}\vert^{-1}_{\hat{g}(\tau)}$ fails the balance law, because its $\tau$-dependence through $a(\tau)$ adds $\partial_\tau$ terms (checked symbolically).
* **Replacement.** Use $\mathcal{F} = c_{\mathcal{F}}\,e^{-3H_0\tau}\ln(\varrho_0/\varrho)$ ($c_{\mathcal{F}} > 0$, $\varrho_0 > 0$).
  * $\ln\varrho$ is planar-harmonic and independent of $x^3$, so $\nabla^2\mathcal{F} = 0$ for every $a$.
  * The balance law $\partial_\tau\mathcal{F} + \theta\mathcal{F} = 0 = D_{\mathcal{F}}\nabla^2\mathcal{F}$ is therefore exact.
  * $J_E^\mu\nabla_\mu\mathcal{F} = -c_{\mathcal{F}}H_0 e^{-3H_0\tau} < 0$.
  * $\mathcal{F}$ is $C^2$ on $\mathcal{M}$, which avoids the axis.

**Global potential, control field, stress.**
* **Potential.** $\Phi = \tfrac{c_\Phi}{6}((x^1)^2 + (x^2)^2 - 2(x^3)^2)$ ($c_\Phi \neq 0$) gives a diagonal $\hat{\Pi} \not\equiv 0$ with in-plane entries $\hat{\Pi}_{11} = \hat{\Pi}_{22} = \pi_\perp(\tau) \equiv \tfrac{c_\Phi}{9}(1 + 2e^{3a(\tau)}) \neq 0$.
  * This corrects the transmitted $\tfrac{2c_\Phi}{9}(1 + e^{3a})$, which gives $4c_\Phi/9$ instead of the correct $c_\Phi/3$ at $a = 0$.
* **Control field.** $\eta = (\omega_0/\pi_\perp)(-x^2, x^1, 0)$ ($\omega_0 \neq 0$). Then $\xi = \omega_0(-x^2\,dx^1 + x^1\,dx^2) \not\equiv 0$, with $d\xi = 2\omega_0\,dx^1 \wedge dx^2$.
* **Stress.** $\partial_{(\mu}\xi_{\nu)} = 0$ and $\nabla\cdot\xi = 0$, so $T^{\mathrm{mat}} = 0 = G$ for any $\kappa_G$. The elliptic vector condition holds because $\nabla^2\xi = 0$ and the Ricci tensor vanishes.
* **Caveat.** $\xi^\mu$ is a rotational Killing field of $g$ (the $x^1x^2$ block is isotropic). This is the trivial case flagged in the r1 review. $\hat{\Pi}$, $\eta$, $\xi$ are non-zero, but **$T^{\mathrm{mat}} \equiv 0$ and $\kappa_G$ remains unexercised**. On flat slices this cannot be avoided, because $G = 0$ forces $T^{\mathrm{mat}} = 0$. Exercising $\kappa_G$ requires a model with curved slices.

**Relational edge.**
* **Coupling operator.** $\Phi^{(j)} = \tfrac{1}{2}((x^1)^2 - (x^2)^2)$ still has a $g$-trace-free Hessian, since $g^{11} = g^{22}$. So $J_{[1\to 2]} = a_\eta\,dx^1$ with $a_\eta = a_0 e^{3H_0\tau/2}$, and $M^{(12)} = \gamma_M a_\eta^2(\delta_{\mu 1}\delta_{\nu 1} - \tfrac{1}{3}g^{11}g_{\mu\nu}) \neq 0$ everywhere.
* **Flux under shear: a new constraint, not in the transmitted model.** The shear stretches the overlap ellipsoid in $g$-geometry. The flux is $\oint_{\partial E} S\,\hat{n}\hat{n}\,dA = \gamma_M a_\eta^2\,e^{-a}\,C_E(b_1 e^{a/2}, b_2 e^{a/2}, b_3 e^{-a})$.
  * For semi-axes $(0.2, 1, 1)$, $e^{-a}C_E$ takes the values $3.64,\ 1.47,\ 0.40,\ -0.10$ at $a = 0,\ 0.5,\ 1.0,\ 1.5$. It changes sign at $a^* \approx 1.365$.
  * Since $a(\tau)$ increases to $a_\infty$, $d\mathcal{I}/d\tau > 0$ for all $\tau$ requires $a_\infty = 2s_\sigma/\gamma_\sigma < a^*$. For example, $s_\sigma = 0.2H_0$ with $\gamma_\sigma \ge H_0$ gives $a_\infty \le 0.4$.
* **Saturation constant.** It becomes $s_0 = k_{\mathcal{I}}\gamma_M a_0^2\,e^{-a_\infty}C_E^\infty/(3H_0\,\mathrm{Vol}_\delta(\mathcal{M}))$, with $C_E^\infty \equiv C_E(b_1 e^{a_\infty/2}, b_2 e^{a_\infty/2}, b_3 e^{-a_\infty})$.
* **Overlap divergence.** $Q_2 = \mathrm{Vol}_g(E)^{-1}(1 + \delta_2 e^{-\gamma_Q(\tau-\tau_0)}u_E)$ with $u_E \in C^\infty_c(E)$, $\int_E u_E\sqrt{\vert g\vert}\,d^3x = 0$ (the normalization condition; on the flat model this is $\int_E u_E\,d^3x = 0$), $u_E \not\equiv 0$, and $\vert\delta_2 u_E\vert < 1$. Then $Q_2^{\vert 12} = Q_2$, and $D_{\mathrm{KL}}(Q_1^{\vert 12} \parallel Q_2^{\vert 12}) > 0$ for finite $\tau$, tending to $0$.
* **Joint density (replaces the §5.5 block construction).**
  * Map each $Q_i$ to the uniform density on $(0,1)^3$ by its Rosenblatt transform.
  * Couple the three coordinate pairs by a Gaussian copula with common correlation $\rho(\tau)$.
  * This gives exact marginals, and $\mathcal{I} = -\tfrac{3}{2}\ln(1-\rho^2)$, because mutual information is invariant under the bijections. Hence $\rho = \sqrt{1 - e^{-2\mathcal{I}/3}}$.
  * **Smoothness fix.** $\rho$ is not differentiable where $\mathcal{I} = 0$, so start from $\mathcal{I}(\tau_0) = \mathcal{I}_0 > 0$ rather than $0$. The offset does not affect the asymptotic saturation. Then $\rho(\tau) \in (0,1)$ is smooth, and $Q_{12}$ is $C^\infty$ in $\tau$.

**Gauge sector.**
* **Setup.** $SU(2)$ with $\hat{T}_a = \sigma_a/2$, $\hat{u} = \hat{T}_3$, so $\hat{\chi} = \chi(\tau)\hat{T}_3$. The connection is $A_1 = b_1 x^2\hat{T}_3$, $A_2 = e^{-\gamma_\sigma(\tau-\tau_0)}b_2 x^1\hat{T}_1$, $A_3 = 0$ ($b_1, b_2 \neq 0$).
* **Curvature.** $F^{\mathrm{YM}}_{12} = -b_1\hat{T}_3 + e^{-\gamma_\sigma(\tau-\tau_0)}(b_2\hat{T}_1 + g_{\mathrm{YM}}b_1 b_2 x^1 x^2\hat{T}_2) \not\equiv 0$, tending to $-b_1\hat{T}_3$.
* **Impedance gradient.** $\hat{\mathcal{E}}_1 = 0$ and $\hat{\mathcal{E}}_2 = -g_{\mathrm{YM}}\chi\,e^{-\gamma_\sigma(\tau-\tau_0)}b_2 x^1\hat{T}_2 \not\equiv 0$, which tends to $0$ in $C^1$.
* **Commutator.** $[F^{\mathrm{YM}}_{12}, \hat{\chi}] = i\chi\,e^{-\gamma_\sigma(\tau-\tau_0)}(g_{\mathrm{YM}}b_1 b_2 x^1 x^2\hat{T}_1 - b_2\hat{T}_2) \not\equiv 0$, tending to $0$.
* **Checks.** The identity $-ig_{\mathrm{YM}}[F_{12}, \hat{\chi}] = D_1\hat{\mathcal{E}}_2 - D_2\hat{\mathcal{E}}_1$ was verified symbolically. $A_\mu$ is $C^1$ and uniformly bounded.

**Harmonic current.** $c_{\mathrm{harm}}\,d\varphi$ remains harmonic, and the absolute boundary conditions still hold.
* Because $g^{11} = g^{22}$, the Laplacian on $x^3$-independent functions is proportional to the planar one.
* The $g$-normal on the axisymmetric boundary stays in the meridian plane.

**Still trivial in §5.8.**
* **Stress sector.** $T^{\mathrm{mat}} \equiv 0$ and $\kappa_G$ is unexercised; this needs curved slices.
* **Surprisal sector.** $J_E^\mu\nabla_\mu q = 0$, so $\partial_\tau\mathcal{H} = 0$, $\mathcal{A}_{\mathcal{M}} = 0$, and the $O_\Omega$ generator equivalence holds with both sides zero.
* **What it would take.** Switching on the surprisal sector needs a non-constant $Q$ from a finite-rank Neumann projection, with $\mathcal{H}$ and $\mathcal{H}_{\mathrm{sol}}$ rebuilt around it. §5.10 does this. §5.9 activates the stress sector, but only in a model that provably fails $O_7$.

### 5.9 Curved slices: cigar $\times\,\mathbb{R}$ activates $\kappa_G$ but cannot satisfy $O_7$ (r7)
**Result.** The transmitted cigar model, with one correction, satisfies every *stress-sector* requirement with $T^{\mathrm{mat}} \not\equiv 0$. However, **no** hysteresis field on cigar $\times\,\mathbb{R}$ meets $O_7$, so this model does not establish joint satisfiability with the stress sector active. All claims below were checked symbolically (exact, sympy) except the obstruction, which is proved by hand.

**Metric.** $g = e^{2H_0\tau}\bar{g}$, with $\bar{g} = w^{-1}((dx^1)^2 + (dx^2)^2) + (dx^3)^2$ and $w \equiv 1 + k_0^2\varrho^2$.
* **Curvature (confirmed).** $R_{ab} = 2k_0^2 w^{-2}\delta_{ab}$, $R = 4k_0^2 e^{-2H_0\tau}/w > 0$, $G_{ab} = 0$, $G_{33} = -2k_0^2/w$.
* **Weyl split (confirmed).** $\Omega = e^{H_0\tau}w^{-1/3}$, $\hat{g} = \mathrm{diag}(w^{-1/3}, w^{-1/3}, w^{2/3})$, $\hat{h} = 0$.
* **Precision (confirmed).** $\Phi = -\tfrac{3}{4}(x^3)^2$ gives $\hat{\Pi} = \mathrm{diag}(\tfrac{1}{2w}, \tfrac{1}{2w}, -1)$.

**Correction: the control field was a factor of 2 too small.** The cigar is a steady gradient soliton with $R_{\mu\nu} = \bar{\nabla}_\mu\bar{\nabla}_\nu \ln w$, not $\tfrac{1}{2}\bar{\nabla}\bar{\nabla}\ln w$.
* **As transmitted.** $\eta = \tfrac{2k_0^2}{\kappa_G}(x^1, x^2, 0)$ gives $\xi = \tfrac{1}{2\kappa_G}d\ln w$ and $\kappa_G\nabla_{(\mu}\xi_{\nu)} = \tfrac{1}{2}R_{\mu\nu}$, so $G \neq \kappa_G T^{\mathrm{mat}}$.
* **Corrected.** $\eta = \tfrac{4k_0^2}{\kappa_G}(x^1, x^2, 0)$ gives $\xi = \tfrac{1}{\kappa_G}d\ln w$. Then, exactly:
  * $R_{\mu\nu} = \kappa_G\nabla_{(\mu}\xi_{\nu)}$ and $G = \kappa_G T^{\mathrm{mat}}$, with $T^{\mathrm{mat}} = \mathrm{diag}(0, 0, -2k_0^2/(\kappa_G w)) \not\equiv 0$;
  * the elliptic vector condition $\nabla^2\xi + \mathrm{Ric}\cdot\xi = 0$;
  * the $\theta$-equation, via $-\kappa_G\partial_\tau(\nabla\cdot\xi) = 2H_0 R$.

**Other transmitted claims (confirmed).**
* **Flux.** $J_E^a = H_0 x^a\,w\ln w/(k_0^2\varrho^2)$, $J_E^3 = H_0 x^3$ gives $\nabla\cdot J_E = 3H_0$.
* **Free energy.** $\ln(\varrho_0/\varrho)$ is harmonic for $g$, so the balance law holds exactly. $J_E\cdot\nabla\ln(\varrho_0/\varrho) = -H_0 w\ln w/(k_0^2\varrho^2) < 0$.
* **Harmonic current.** $c_{\mathrm{harm}}\,d\varphi$ remains harmonic with absolute boundary conditions (the planar block is conformally flat and axisymmetric).

**Obstruction to $O_7$ (proof).** Here $\hat{h} = 0$, so $\hat{\rho}_g = \tfrac{1}{3}\delta$ for all $\tau$. Since $\hat{g}_\infty = \hat{g}$ is pointwise proportional to $\bar{g}$, the condition $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) \to 0$ forces the limiting hysteresis to satisfy $\bar{\nabla}\bar{\nabla}\mathcal{H}_\infty = \lambda\bar{g}$ with $\lambda > 0$.
* **Step 1 (splitting).** On the product, the mixed components give $\partial_a\partial_3\mathcal{H}_\infty = 0$, so $\mathcal{H}_\infty = A(x^1, x^2) + B(x^3)$.
* **Step 2 ($\lambda$ is constant).** $B'' = \lambda$ and $\mathrm{Hess}_{\mathrm{cig}}A = \lambda\bar{g}_{\mathrm{cig}}$ make $\lambda$ a function of $x^3$ alone and of $(x^1, x^2)$ alone, hence constant.
* **Step 3 (contradiction).** Take the divergence of $\mathrm{Hess}_{\mathrm{cig}}A = \lambda\bar{g}$. Since $\Delta A = 2\lambda$ is constant, this gives $K\,\nabla A = 0$. The Gaussian curvature $K = 2k_0^2/w > 0$, so $\nabla A = 0$, which contradicts $\lambda > 0$.

The argument is local, so it applies on every subdomain and does not depend on how $\mathcal{H}$ evolves in time. Gemini's note ("Tashiro") pointed at this; the conclusion is that the obstruction is real and cannot be removed by choosing $\mathcal{H}$ differently.

**Also not addressed for the cigar.** The relational edge was not recomputed on the curved metric:
* $\hat{\Pi}^{(j)}$ for $\Phi^{(j)} = \tfrac{1}{2}((x^1)^2 - (x^2)^2)$ picks up Christoffel terms, which changes $M^{(12)}$ and the flux sign analysis of §5.5 and §5.8.
* Geodesic convexity of the coordinate ellipsoid $E$ is no longer automatic (it holds for $E$ small enough).

**Candidate route (not verified).** Use a rotationally symmetric steady gradient soliton: the Bryant soliton, $\bar{g} = dr^2 + w(r)^2 g_{S^2}$.
* **Why the hysteresis obstruction disappears.** Any radial $f$ with $f' = w$ satisfies $\bar{\nabla}\bar{\nabla}f = w'\bar{g}$, which is $\succ 0$ because $w' > 0$. With $\hat{h} = 0$, this gives $\hat{\rho}_{\mathcal{H}} = \hat{\rho}_g$ exactly.
* **Why the stress sector still works.** $\xi = \kappa_G^{-1}\nabla h$ from the soliton potential gives $T^{\mathrm{mat}} \not\equiv 0$.
* **Remaining construction.** Take $\mathcal{M}$ to be a smooth solid torus away from the tip, so that $H^1 \neq 0$; the harmonic field then exists by Hodge–Morrey–Friedrichs. Choose $\Phi$ radial with $\Phi'' \neq \Phi' w'/w$ so that $\hat{\Pi}$ is invertible, and set $\eta = \hat{\Pi}^{-1}\xi$.
* **Not closed form.** The soliton is an ODE solution. Its needed properties ($0 < w' < 1$, $w'' < 0$) follow from positive sectional curvature, but this route has not been checked in detail.

### 5.10 Active surprisal sector, $J_E^\mu\nabla_\mu q \not\equiv 0$ (r7)
**Correction to the transmitted version.** With constant $\varepsilon_q$, $S_q \equiv J_E^\mu\nabla_\mu q$ is $\tau$-independent, so $\mathcal{H} = \mathcal{H}_0 + (\tau - \tau_0)S_q$.
* **The defect.** As $\tau \to \infty$, $\hat{\rho}_{\mathcal{H}}$ tends to the normalized $\mathrm{Hess}\,S_q$. On flat slices, $O_7$ then forces $\mathrm{Hess}\,S_q = \lambda\delta$ with constant $\lambda > 0$ (the same divergence argument as in §5.9), i.e., $S_q$ an exact positive quadratic.
* **Why it fails.** For $q = -\ln(v_0Q)$ built from Neumann modes, $S_q$ involves logarithms of trigonometric/Bessel products, which are not quadratic. So $\mathrm{Hess}\,\mathcal{H}$ eventually loses positive-definiteness and $O_7$ fails.
* **Why the finite-interval option doesn't help.** Restricting to $\tau \le \tau_{\max}$ is not an option, since the hypotheses are asymptotic.

**Repaired construction (flat isotropic model of §5.1–5.6).**
* **State.** $\rho_{\mathrm{total}} = (1-\varepsilon_q)\vert\phi_0\rangle\langle\phi_0\vert + \varepsilon_q\vert\phi_1\rangle\langle\phi_1\vert$ with **decaying** weight $\varepsilon_q(\tau) = \varepsilon_0 e^{-\gamma_q(\tau-\tau_0)}$, $0 < \varepsilon_0 < 1$.
  * $\phi_k = e^{-3H_0\tau/2}\bar{\phi}_k$, where $\bar{\phi}_1$ is a non-constant Neumann mode with $\bar{\lambda}_1 e^{-2H_0\tau_0} \le \Lambda_{\mathrm{gate}}^2$.
  * The gate therefore passes both modes for all $\tau \ge \tau_0$, and $\rho_{\mathrm{local}} = \rho_{\mathrm{total}}$.
* **Density.** $Q = e^{-3H_0\tau}((1-\varepsilon_q)/\bar{V} + \varepsilon_q\bar{\phi}_1^2) > 0$, normalized.
* **Surprisal source.** $S_q = J_E\cdot\nabla q = -H_0\,x\cdot\nabla\ln((1-\varepsilon_q)/\bar{V} + \varepsilon_q\bar{\phi}_1^2) \not\equiv 0$ for $\varepsilon_q > 0$. It is $O(\varepsilon_q)$ in $C^2$.
* **Hysteresis.** Choose the initial value so the limit is quadratic: $\mathcal{H}(\tau, \mathbf{x}) = \tfrac{c_{\mathcal{H}}}{2}\vert\mathbf{x}\vert^2 - \int_\tau^\infty S_q(\tau', \mathbf{x})\,d\tau'$. Then:
  * $\partial_\tau\mathcal{H} = S_q$ ($O_0$);
  * $\mathrm{Hess}\,\mathcal{H} = c_{\mathcal{H}}\delta - O(\varepsilon_0/\gamma_q) \succ 0$ for $\varepsilon_0/\gamma_q$ small;
  * $\hat{\rho}_{\mathcal{H}} \to \tfrac{1}{3}\delta = \hat{\rho}_g$, so $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) > 0$ for finite $\tau$, tending to $0$ ($O_7$).
* **Ultralocal solution ($O_\Omega$).** On the homothetic flat model, $\ln\sqrt{\det g} = 3H_0\tau$, so $\tau(g) \equiv \ln\sqrt{\det g}/(3H_0)$ is an ultralocal function of $g$. Set $\mathcal{H}_{\mathrm{sol}}(g, \mathbf{x}) \equiv \mathcal{H}(\tau(g), \mathbf{x})$.
  * Then $\partial\mathcal{H}_{\mathrm{sol}}/\partial g_{\mu\nu} = S_q\cdot\partial\tau/\partial g_{\mu\nu} = \tfrac{1}{2}(S_q/(3H_0))g^{\mu\nu}$, which is exactly the $O_\Omega$ right-hand side, and its trace-free part is $0$.
  * This generalizes the transmitted $\tfrac{S_q}{3H_0}\ln\sqrt{\det g}$ ansatz to $\tau$-dependent $S_q$.
* **Functional.** $\Psi = \int_{\mathcal{M}}(\mathcal{H} - \mathcal{H}_{\mathrm{sol}}[g])\,d^3x$ gives $\delta\Psi/\delta\mathcal{H} = 1 \neq 0$, and the locus condition holds identically.
  * $\hat{\mathbb{L}}_{\mathrm{stat}}\Psi = -2H_0 g_{\mu\nu}\tfrac{S_q}{6H_0}g^{\mu\nu} + S_q = 0$.
  * Both sides of the generator equivalence are now non-zero at every finite $\tau$, so the equivalence is exercised non-trivially.
* **Remaining data.** Take $P = Q(1 + \epsilon(\tau)u)$ as in §5.4.

**Status after r7.**
* **Surprisal sector (§5.10).** Active and jointly satisfiable on the flat model.
* **Shear, gauge, overlap and $\hat{\Pi}$ sectors (§5.8).** Active, in separate constructions.
* **Stress sector.** Active only on the cigar (§5.9), where $O_7$ provably fails.
* **Open problems.**
  1. Exhibit a curved-slice model satisfying $O_7$; §5.9 suggests the Bryant-soliton route.
  2. Combine all sectors in a single configuration.

### 5.11 Consolidated model: all sectors active on an exact warped soliton (r8)
This section closes both open problems of §5.10. The construction was transmitted by Gemini Argon 4 and verified symbolically here (exact sympy, both with and without shear), with two corrections.

**Domain.** $\mathcal{M}$ is the rounded hollow cylinder $\{R_1 \le \varrho \le R_2,\ z_1 \le z \le z_2\}$ with $z \equiv x^3$ and $z_1 > 0$. It is compact and connected, with $H^1_{\mathrm{dR}} \cong \mathbb{R}$.

**Metric.** $g = e^{2H_0\tau}\,\mathrm{diag}\big(z^{\sqrt{2}}e^{a(\tau)},\ z^{\sqrt{2}}e^{a(\tau)},\ e^{-2a(\tau)}\big)$, where:
* $a(\tau) = (2s_\sigma/\gamma_\sigma)(1 - e^{-\gamma_\sigma(\tau-\tau_0)})$ with $0 < s_\sigma < H_0/2$;
* $a \equiv 0$ recovers the unsheared soliton $\bar{g} = z^{\sqrt{2}}((dx^1)^2 + (dx^2)^2) + dz^2$, a warped product with flat fiber and warping $w = z^{1/\sqrt{2}}$.

**Correction 1: use axisymmetric shear.** The transmitted planar shear $\hat{h} = a\,\mathrm{diag}(1,-1,0)$ preserves the stress sector, but it destroys the harmonicity of $d\varphi$ (the $O_5$ harmonic current) and of $\ln\varrho$; both were checked symbolically.
* The axisymmetric shear $\hat{h} = a\,\mathrm{diag}(1,1,-2)$ keeps every closed-form object.
* It is locally isometric to the unsheared soliton by constant rescalings of $x^{1,2}$ and $z$.

**Weyl split and kinematics.**
* $\Omega = e^{H_0\tau}z^{\sqrt{2}/3}$, $\hat{g} = \mathrm{diag}(z^{\sqrt{2}/3}, z^{\sqrt{2}/3}, z^{-2\sqrt{2}/3})$ with $\det\hat{g} = 1$, $\hat{h} = a\,\mathrm{diag}(1,1,-2)$.
* $\theta = 3H_0$.
* $\sigma^\mu_{\;\nu} = s_\sigma e^{-\gamma_\sigma(\tau-\tau_0)}\,\mathrm{diag}(1,1,-2)$.
* $\lambda_{\min}(\mathcal{D}) \ge H_0 - 2s_\sigma > 0$.
* $\chi = 1 + 2s_\sigma^2 e^{-2\gamma_\sigma(\tau-\tau_0)}/H_0^2$.
* $G_\infty = \hat{g}_\infty$ up to the conformal factor, and $\succ 0$.

**Curvature (confirmed).**
* $R = (2\sqrt{2} - 3)\,e^{-2H_0\tau}/z^2 < 0$ (shown for $a = 0$; $a \ne 0$ only rescales by $e^{\pm a}$ factors).
* $G_{33} = 1/(2z^2)$ and $G_{ab} = -\frac{\sqrt{2}-1}{2z^2}\bar{g}_{ab}$, so all three diagonal components are non-zero.

**Stress sector, active (confirmed with and without shear).**
* $\Phi = \tfrac{3}{4}z^2$ gives $\hat{\Pi}_{33} = 1 - \tfrac{1}{\sqrt{2}}$, which is $\tau$-independent even under shear.
* $\eta = (0, 0, -\sqrt{2}/(\kappa_G z))$ gives $\xi = -\frac{\sqrt{2}-1}{\kappa_G z}\,dz$.
* Then, exactly:
  * $R_{\mu\nu} = \kappa_G\nabla_{(\mu}\xi_{\nu)}$;
  * $G_{\mu\nu} = \kappa_G T^{\mathrm{mat}}_{\mu\nu} \not\equiv 0$;
  * $\nabla^2\xi + \mathrm{Ric}\cdot\xi = 0$.
* $\kappa_G$ is genuinely exercised.

**Shear coupling, active.**
* $\theta$ is constant, so the $\tau$-compatibility law reduces to $\kappa_G\partial_\tau T^{\mathrm{mat}} = \mathbb{L}_{\mathrm{Ein}}[\sigma]$.
* It was verified that $\mathbb{L}_{\mathrm{Ein}}[\sigma]_{\mu\nu} = \partial_\tau G_{\mu\nu}$, with non-zero planar components ($\propto \dot{a}$) and $\mathbb{L}_{\mathrm{Ein}}[\sigma]_{33} = 0$.
* The elliptic $\theta$-equation holds.

**Flux and free energy.**
* **Correction 2: the flux coefficient.** The transmitted $J_E = (\tfrac{3-\sqrt{2}}{2}H_0x^1, \tfrac{3-\sqrt{2}}{2}H_0x^2, H_0z)$ gives $\nabla\cdot J_E = 4H_0$, not $3H_0$; the planar terms contribute $(3-\sqrt{2})H_0$, not $(2-\sqrt{2})H_0$. The correct coefficient is $\tfrac{2-\sqrt{2}}{2}$: $J_E = (\tfrac{2-\sqrt{2}}{2}H_0x^1, \tfrac{2-\sqrt{2}}{2}H_0x^2, H_0z)$ has $\nabla\cdot J_E = 3H_0$ exactly, at all $a$.
* **Free energy.** $\mathcal{F} = c_{\mathcal{F}}e^{-3H_0\tau}z^{1-\sqrt{2}}$ is harmonic at all $a$. Then $J_E\cdot\nabla\mathcal{F} = -(\sqrt{2}-1)H_0 c_{\mathcal{F}}e^{-3H_0\tau}z^{1-\sqrt{2}} < 0$, unaffected by Correction 2.
* **Harmonic current.** $c_{\mathrm{harm}}\,d\varphi$ remains harmonic, and the absolute boundary conditions hold (the planar block is isotropic).

**Hysteresis and $O_7$ (no obstruction).**
* $\mathcal{H}_0 = \frac{c_{\mathcal{H}}}{1+1/\sqrt{2}}z^{1+1/\sqrt{2}}$ satisfies $\nabla\nabla\mathcal{H}_0 \propto g$ with a positive factor at every $\tau$ (verified with shear). Therefore $\hat{\rho}_{\mathcal{H}_0} = \hat{\rho}_g$ exactly.
* The §5.9 obstruction does not apply, because the warped product has $\mathcal{H}_0' \propto w$ and $w' > 0$.

**Surprisal sector (§5.10 construction, transplanted).**
* **State.** $\rho_{\mathrm{total}} = (1-\varepsilon_q)\vert\phi_0\rangle\langle\phi_0\vert + \varepsilon_q\vert\phi_1\rangle\langle\phi_1\vert$ with $\varepsilon_q = \varepsilon_0 e^{-\gamma_q(\tau-\tau_0)}$, where $\phi_1$ is a non-constant Neumann mode of $-\nabla^2_{g(\tau)}$.
* **Hysteresis.** $\mathcal{H} = \mathcal{H}_0 - \int_\tau^\infty S_q\,d\tau'$.
* **Ultralocal solution.** $\mathcal{H}_{\mathrm{sol}}(g, \mathbf{x}) = \mathcal{H}(\tau(g, \mathbf{x}), \mathbf{x})$ with $\tau(g, \mathbf{x}) = \ln(\sqrt{\det g}/z^{\sqrt{2}})/(3H_0)$. Shear does not change $\det g$, so $\partial\mathcal{H}_{\mathrm{sol}}/\partial g_{\mu\nu} = \tfrac{1}{2}(S_q/(3H_0))g^{\mu\nu}$ exactly.
* **Consequences.** The $O_\Omega$ generator equivalence is exercised non-trivially. $\mathrm{Hess}\,\mathcal{H} \succ 0$ for $\varepsilon_0/\gamma_q$ small, and $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) > 0$ for finite $\tau$, tending to $0$.

**Relational edge.**
* **Coupling.** $\Phi^{(1)} = \Phi^{(2)} = \tfrac{3}{4}z^2$ and $\eta_{1\to 2} = -\eta_{2\to 1} = \frac{a_0e^{3H_0\tau/2}}{1-1/\sqrt{2}}\,\partial_z$ give $J_{[1\to 2]} = a_0e^{3H_0\tau/2}\,dz$, $F = 0$, and $M^{(12)} = \gamma_M a_0^2 e^{3H_0\tau}(\delta_{\mu 3}\delta_{\nu 3} - \tfrac{1}{3}g^{33}g_{\mu\nu}) \neq 0$ everywhere.
* **Overlap.** Take $\mathcal{U}_2 = E$, a small coordinate ellipsoid flattened along $z$.
  * The axisymmetric shear compresses $z$ physically ($g_{33} \propto e^{-2a}$, $a \ge 0$), so $E$ only becomes *more* oblate along the coupling direction. Unlike §5.8, no threshold $a^*$ arises.
  * Flux positivity and geodesic convexity are argued for $E$ small, where curvature corrections are $O(\mathrm{diam}\,E)$. This is the standard small-domain argument, not Whitehead's theorem, which concerns geodesic balls. It was not computed numerically on the curved metric.
* **Overlap divergence and gauge sector.** Carried over unchanged from §5.8.
  * The gauge sector depends only on $\chi(\tau)$, which is spatially constant here.
  * Use the Gaussian-copula $Q_{12}$ with $\mathcal{I}(\tau_0) > 0$.

**Status after r8.** Both open problems of §5.10 are closed.
* A curved-slice model with $G = \kappa_G T^{\mathrm{mat}} \not\equiv 0$ satisfies $O_7$.
* A single configuration has every sector active simultaneously: curved stress, shear with $\mathbb{L}_{\mathrm{Ein}}[\sigma] \not\equiv 0$, $\chi > 1$, $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) > 0$, gauge curvature with $\hat{\mathcal{E}} \not\equiv 0$, overlap divergence, and active surprisal.

**Not elementary, contrary to the transmission.** The metric, stress, flux, free energy, harmonic current and $\mathcal{H}_0$ are closed-form. The Neumann mode $\phi_1$ (and hence $Q$, $S_q$, $\mathcal{H}$), the Rosenblatt maps in $Q_{12}$, and the small-$E$ flux bound exist but are not explicit.

**Remaining checks.**
* A numerical flux computation on the curved metric.
* A careful written verification of the whole combined configuration in one place: the components were verified sector by sector.

### 5.12 Numerical flux, convexity, and end-to-end verification of §5.11 (r9)
The two remaining checks of §5.11 are now done. All numbers below come from `flux.py` and `convex.py`, and the full configuration is checked by `e2e_5_11.py` (36/36 checks pass, about 15 s).

**Flux integrand.** The coupling tensor is $S^{(12)} = \gamma_M a_\eta^2(\delta_{\mu 3}\delta_{\nu 3} - \tfrac{1}{3}g^{33}g_{\mu\nu})$. Write $\nu$ for the Euclidean unit covector normal, $\hat{n}^\mu = g^{\mu\nu}\nu_\nu/\vert\nu\vert_{g^{-1}}$, and $dA_g = \sqrt{\vert g\vert}\,\vert\nu\vert_{g^{-1}}\,dA_\delta$. All $\tau$-factors cancel, and
$$\frac{\oint_{\partial E}S^{(12)}_{\mu\nu}\hat{n}^\mu\hat{n}^\nu dA}{\gamma_M a_\eta^2} \equiv C(a) = \oint_{\partial E} e^{3a/2}z^{\sqrt{2}/2}\,\frac{\tfrac{2}{3}e^{3a}z^{\sqrt{2}}\nu_3^2 - \tfrac{1}{3}(\nu_1^2+\nu_2^2)}{\sqrt{\nu_1^2+\nu_2^2+e^{3a}z^{\sqrt{2}}\nu_3^2}}\,dA_\delta .$$
* **Validation.** This closed form agrees to all printed digits with a brute-force evaluation built from the induced metric and the $g$-unit normal.
* **Correction to the transmitted integrand.** The transmitted $C_E^{\mathrm{warped}}$ places $z^{\sqrt{2}}$ on the wrong components: it contracts with $g_{ab}$ where $g^{ab}$ is required. It differs numerically, for example $0.517$ versus the correct $0.654$ at $a = 0$ for semi-axes $(0.25, 0.25, 0.05)$. Its sign is nonetheless also positive throughout.

**Flux is positive.** $C(a) > 0$ for every tested ellipsoid flattened along $z$, over $a \in [0, 8]$. Because the shear compresses $z$, $C(a)$ increases with $a$.

| semi-axes | $C(0)$ | $C(0.5)$ | $C(1)$ | $C(2)$ |
|---|---|---|---|---|
| $(0.25, 0.25, 0.05)$ | $0.654$ | $3.07$ | $13.9$ | $281$ |
| $(0.2, 0.2, 0.04)$ | $0.419$ | $1.96$ | $8.92$ | $180$ |

**Convexity is not automatic; this corrects §5.11's "small $E$" argument.** Strict positivity of the Riemannian second fundamental form of $\partial E$ in $g$ was checked directly. The smallest principal curvature is computed from $\mathrm{Hess}_g F\vert_{T\partial E}/\vert\nabla F\vert_g$ with $F = \sum_i((x - c)_i/b_i)^2 - 1$, over a dense surface grid.
* **Why it can fail.** Near its bottom pole, a flat ellipsoid is nearly a level set $z = $ const. In this warped metric those level sets bend away from the bottom face, with a contribution $-\Gamma^3_{ab}\partial_3 F \propto e^{3a}$.
* **Criterion.** Convexity therefore holds only while $a < a_c$, with
$$a_c \approx \tfrac{1}{3}\ln\!\big(b_3/(p\,z_0^{\sqrt{2}-1}b_1^2)\big), \qquad p = 1/\sqrt{2},\ z_0 = 2.$$
The numerical thresholds match this estimate to within $0.3\%$.

| semi-axes | numerical $a_c$ | estimate |
|---|---|---|
| $(0.25, 0.25, 0.05)$ | not convex at $a = 0$ | $-0.055$ |
| $(0.2, 0.2, 0.04)$ | $0.023$ | $0.020$ |
| $(0.1, 0.1, 0.02)$ | $0.252$ | $0.251$ |
| $(0.05, 0.05, 0.01)$ | $0.483$ | $0.482$ |
| $(0.1, 0.1, 0.05)$ | $0.560$ | $0.556$ |
| $(0.05, 0.05, 0.025)$ | $0.789$ | $0.787$ |
| $(0.02, 0.02, 0.01)$ | $1.094$ | $1.093$ |

* **Consequence.** Both transmitted example ellipsoids fail for essentially any shear: $(0.25, 0.25, 0.05)$ is not convex even at $a = 0$, and $(0.2, 0.2, 0.04)$ only up to $a \approx 0.023$. The hypothesis "$\mathcal{U}_{12}$ geodesically convex for all $\tau$" requires $a_\infty = 2s_\sigma/\gamma_\sigma < a_c(E)$. The overlap must therefore be chosen *after* the shear parameters, and its size must shrink like $e^{-3a_\infty/2}$ at fixed aspect ratio.

**Recommended concrete choice.**
* **Parameters.** $s_\sigma = 0.2H_0$ and $\gamma_\sigma = H_0$, so $a_\infty = 0.4$. Take $E$ centered at $(2, 0, 2)$ with semi-axes $(0.05, 0.05, 0.025)$, inside $\mathcal{M} = \{1 \le \varrho \le 3,\ 1 \le z \le 3\}$.
* **Flux.** $C(a)$ increases from $0.0213$ to $0.0833$ over $a \in [0, 0.4]$, and $C_\infty = C(0.4) = 0.0833$.
* **Convexity.** The minimum principal curvature over $a \in [0, 0.4]$ is $1.18 > 0$, and $a_c = 0.79 > a_\infty$.
* **Geodesic convexity.** $\mathrm{II} \succ 0$ gives local convexity: minimizing geodesics between points of $\bar{E}$ stay in $\bar{E}$. $E$ has diameter $0.1$, far below the curvature scale ($\vert\mathrm{Riem}\vert \sim 0.1$ near $z = 2$), so geodesics are also unique. This last step is a scale argument; no conjugate-point computation was done.

**Saturation constant.** With $a_\eta = a_0e^{3H_0\tau/2}$, $d\mathcal{I}/d\tau = k_{\mathcal{I}}\gamma_M a_0^2 e^{3H_0\tau}C(a(\tau))$ and $V_{\mathcal{M}} = e^{3H_0\tau}\int_{\mathcal{M}}z^{\sqrt{2}}d^3x$. Since $C(a(\tau)) \to C_\infty$ exponentially,
$$s_0 = \frac{k_{\mathcal{I}}\gamma_M a_0^2\,C_\infty}{3H_0\int_{\mathcal{M}}z^{\sqrt{2}}\,d^3x} \quad\text{gives}\quad \frac{\mathcal{I}}{s_0V_{\mathcal{M}}} \to 1 .$$
The transmitted alternative $a_\eta = a_0e^{3H_0\tau/2 - a}$ is not needed. With $C$ defined as the whole integral, the transmitted factor $e^{2a_\infty}$ does not appear.

**End-to-end script (`e2e_5_11.py`): what it checks.** The symbolic checks are exact (sympy) with general $s_\sigma, \gamma_\sigma, H_0, \kappa_G$ and the explicit shear profile $a(\tau)$.
* **$O_0$.** $\theta$ in all three forms; $\nabla\cdot J_E = \theta$ with the corrected coefficient. It also records that the transmitted coefficient gives $4H_0$.
* **$O_1$/$O_4$.** The free-energy balance law, and $J_E\cdot\nabla\mathcal{F} < 0$.
* **$O_2$.** The Weyl split, $\det\hat{g} = 1$, $\partial_\tau\ln\Omega = \theta/3$, $\xi = \hat{\Pi}\eta$, $G = \kappa_G T^{\mathrm{mat}}$ with all three diagonal entries non-zero, $R = \kappa_G\nabla\cdot\xi$, the full $\tau$-law $\kappa_G\partial_\tau T^{\mathrm{mat}} = \mathbb{L}_{\mathrm{Ein}}[\sigma] \not\equiv 0$, and the traced $\theta$-equation.
* **$O_3$.** $\sigma$ in closed form, the damping law, tracelessness, and $\hat{h}_\infty$.
* **$O_4$.** $\mathrm{tr}\,T^{\mathrm{mat}}$, and the elliptic condition (hence $\nabla\cdot T^{\mathrm{mat}} = 0$).
* **$O_5$.** $e^{-2H_0\tau}g \to G_\infty \succ 0$, the mixed-rate limit, harmonicity of $d\varphi$, and the absolute boundary condition on an axisymmetric boundary.
* **$O_6$.** $M$ is symmetric and trace-free with mixed spectrum $\gamma_M\vert J\vert^2(\tfrac{2}{3}, -\tfrac{1}{3}, -\tfrac{1}{3})$; $\mathrm{Tr}\,\mathcal{D} = \theta$; $\lambda_{\min}(\mathcal{D}) = H_0 - 2s_\sigma e^{-\gamma_\sigma(\tau-\tau_0)}$; and, numerically, flux positivity and convexity.
* **$O_7$.** The $\chi$ formula, $\hat{\rho}_g \to \tfrac{1}{3}\delta$, $\mathrm{Hess}\,\mathcal{H}_0 = \lambda g$ with $\lambda > 0$, and the gauge identity with $\hat{\mathcal{E}}_2 \not\equiv 0 \to 0$.
* **$O_\Omega$.** For a generic surprisal source $S_q$, $\partial\tau(g,\mathbf{x})/\partial g_{\mu\nu} = g^{\mu\nu}/(6H_0)$ on a generic symmetric matrix, hence $\partial\mathcal{H}_{\mathrm{sol}}/\partial g = \tfrac{1}{2}(S_q/(3H_0))g^{\mu\nu}$ and $\hat{\mathbb{L}}_{\mathrm{stat}}\Psi = 0$.

**What the script does not check.**
* **The Neumann mode.** $\phi_1$ on the rounded, warped, sheared domain is not explicit. Positivity of $Q$, the bound $\mathrm{Hess}\,\mathcal{H} \succ 0$ for small $\varepsilon_0/\gamma_q$, and the magnitude of $S_q$ rest on the qualitative argument of §5.10.
* **The copula.** The Rosenblatt maps of the Gaussian-copula $Q_{12}$ are not computed.
* **The rounded rims.** The rim rounding is not modelled. The boundary-condition check uses a general axisymmetric normal, which covers it.
* **Global uniqueness of geodesics.** In $E$ this rests on the scale argument above.

**Status after r9.** Joint satisfiability of the full hypothesis set, with every sector active, is established by an explicit configuration. Everything closed-form is verified exactly and the overlap geometry numerically, with the caveats listed above. The correction found here is substantive: the overlap $E$ must satisfy $a_\infty < a_c(E)$.

### 5.13 Branch II witness: a bounded, curved, non-equilibrium steady state with relaxing shear (r10)
This section verifies one configuration of the generalized r7 system with $H_0 = 0$. Claims marked *verified* were checked by exact symbolic computation (sympy) in `r10_branch2_witness_check.py`, which is distributed with this document and prints a PASS/FAIL line for each check (40 checks: 36 for the witness, 4 for a Branch I regression). Claims marked *derived* follow from verified quantities by a stated one-line argument and have no PASS line of their own.

**Domain.** The rounded hollow cylinder of §5.11, $\{R_1 \le \varrho \le R_2,\ z_1 \le z \le z_2\}$ with $z_1 > 0$; compact, connected, $H^1_{\mathrm{dR}} \cong \mathbb{R}$.

**Metric.** $g = \mathrm{diag}\big(z^{\sqrt{2}}e^{a(\tau)},\ z^{\sqrt{2}}e^{a(\tau)},\ e^{-2a(\tau)}\big)$: the §5.11 metric with $H_0 = 0$, where $a(\tau) = (2s_\sigma/\gamma_\sigma)(1 - e^{-\gamma_\sigma(\tau-\tau_0)})$ with $s_\sigma = 0.2\gamma_\sigma$, $\gamma_\sigma > 0$, so $a_\infty = 0.4$. The domain and overlap are those of §5.11: $\mathcal{M} = \{1 \le \varrho \le 3,\ 1 \le z \le 3\}$, with $E$ centred at $(2, 0, 2)$ and semi-axes $(0.05, 0.05, 0.025)$, for which §5.12 found convexity for all $a < a_c = 0.79$ and $C(a) > 0$ on $a \in [0, 0.4]$, the range used here ($a \in [0, 0.4]$ throughout). The script treats $a(\tau)$ as an arbitrary function, so every identity below holds for any shear history, except the $O_3$ Eq. [2] damping law, which is checked for the declared exponential $a(\tau)$ only.

**Kinematics (verified).** $\det g = z^{2\sqrt{2}}$ is independent of $a$, so $\theta = 0$ exactly and $\partial_\tau\sqrt{\vert g^{(i)}\vert} = 0$ (verified), which satisfies the r7 form of $O_5$ Eq. [0] ($\ge 0$ in Branch II), $\Omega = z^{\sqrt{2}/3}$ is $\tau$-independent ($O_2$ Eq. [2] with $J_{\mathrm{geom}} = 0$), the $u_{\mathrm{exp}}$ flux identity of $O_7$ Eq. [3] holds with $J_{\mathrm{geom}} = u_{\mathrm{exp}} = 0$ (derived), and the shear $\sigma^\mu_{\;\nu} = \frac{\dot{a}}{2}\mathrm{diag}(1,1,-2)$ (verified) is active and decays; $\sigma^\mu_{\;\nu}\sigma^\nu_{\;\mu} = \frac{3}{2}\dot{a}^2$ (verified) $\to 0$ (derived, since $\dot{a} \to 0$). $J_{\mathrm{geom}} = 0$, $\dot{V}_{\mathcal{M}} = 0$, $\dot{W}_{\mathrm{ext}} = 0$, and $V_{\mathcal{M}} = V_\infty$ for all $\tau$. $\frac{1}{2}g^{-1}\partial_\tau g$ is proportional to $\dot{a}$ and tends to $0$, and $g \to G_\infty$ as $a \to a_\infty$, so $O_5$ Eq. [4] holds with $H_0 = 0$.

**Curved stress sector (verified, with shear).** With $\Phi = \frac{3}{4}z^2$ and $\eta = (0, 0, -\sqrt{2}/(\kappa_G z))$ as in §5.11:
* $\xi = \frac{1-\sqrt{2}}{\kappa_G z}\,dz$, independent of $\tau$;
* $G_{\mu\nu} = \kappa_G T^{\mathrm{mat}}_{\mu\nu} \not\equiv 0$, $R = \kappa_G\nabla_\alpha\xi^\alpha$, and $\nabla^2\xi_\nu + R_\nu^{\;\alpha}\xi_\alpha = 0$;
* the $\tau$-compatibility law $\kappa_G\partial_\tau T^{\mathrm{mat}} = \mathbb{L}_{\mathrm{Ein}}[\sigma]$ (its $\theta$ terms vanish) and the elliptic $\theta$-equation $0 = -\kappa_G\partial_\tau(\nabla_\alpha\xi^\alpha) + 2\nabla^\alpha\nabla^\beta\sigma_{\alpha\beta} - 2\sigma^{\alpha\beta}R_{\alpha\beta}$ both hold exactly at every $\tau$.

So $\kappa_G$ is exercised in a bounded configuration with shear, without any expansion.

**Free energy with anisotropic transport and an interior sink (verified).**
* Declared constitutive terms: $\mathfrak{K}^{\mu\nu} = \mathrm{diag}(k_1, k_1, k_3)$ in coordinate components ($k_1, k_3 > 0$, $k_1 \neq k_3$ in general; positive definite and anisotropic relative to $g$), and a zeroth-order (saturated) sink $\mathcal{R}_{\mathcal{F}} = r_0 > 0$.
* $\mathcal{F}(z)$ with $\partial_z\mathcal{F} = \big(r_0z^{1+\sqrt{2}}/(1+\sqrt{2}) - C_{\mathcal{F}}\big)/(k_3z^{\sqrt{2}})$ is static and satisfies the r7 balance law $0 = \nabla_\mu(\mathfrak{K}^{\mu\nu}\nabla_\nu\mathcal{F}) - \mathcal{R}_{\mathcal{F}}$ exactly (with $\theta = 0$, $\partial_\tau\mathcal{F} = 0$).
* For $C_{\mathcal{F}} > r_0z_2^{1+\sqrt{2}}/(1+\sqrt{2})$, $\partial_z\mathcal{F} < 0$ on all of $[z_1, z_2]$, so $\nabla\mathcal{F} \neq 0$: the numerator $r_0z^{1+\sqrt{2}}/(1+\sqrt{2}) - C_{\mathcal{F}}$ is increasing in $z$ (verified), so its value at $z_2$ (verified negative) bounds it.
* Here $\nabla_\mu J_E^\mu = -r_0/p_0 \neq 0$ while $\theta = 0$ (verified): $J_E$ is not an expansion current in Branch II, which is why every $\theta$ identity uses $J_{\mathrm{geom}}$.

**Throughput (verified).** With the Branch II $J_E^\mu = J_W^\mu/p_0$:
* $J_E^\mu\nabla_\mu\mathcal{F} = -k_3(\partial_z\mathcal{F})^2/p_0 < 0$;
* $\Theta_E = \beta_{\mathrm{th}}k_3(\partial_z\mathcal{F})^2/(p_0s_0)$ (verified), pointwise independent of $\tau$ (verified), and $> 0$ because $\partial_z\mathcal{F} < 0$ (derived); since $\sqrt{\vert g\vert}$ is static, $\langle\Theta_E\rangle_{\mathcal{M}} = \Theta_\infty > 0$ (derived);
* $\dot{W}_{\mathrm{diss}} = (s_0/\beta_{\mathrm{th}})\int\Theta_E\sqrt{\vert g\vert} > 0$ and $\dot{W}_{\mathrm{tot}} > 0$ while $\dot{W}_{\mathrm{ext}} = 0$ (derived);
* $\Theta_{\mathrm{tot}} = \Theta_E$ because $\theta = 0$, so $\tau_\Theta$ increases strictly (derived);
* $\sigma^\mu_{\;\nu}\sigma^\nu_{\;\mu} = \frac{3}{2}\dot{a}^2$ (verified), so $\chi_E = 1 + \frac{9}{2}\dot{a}^2/\Theta_\infty^2 \to 1$ (derived), while $\chi$ itself is undefined ($\theta = 0$), as Decision 6 anticipates.

**Hysteresis and $O_7$ (verified).** $\mathcal{H}_0 = \frac{z^{1+1/\sqrt{2}}}{1+1/\sqrt{2}}$ has $\nabla\nabla\mathcal{H}_0 = \lambda g$ with $\lambda = \frac{\sqrt{2}}{2}z^{-1+\sqrt{2}/2}e^{2a} > 0$ at every $\tau$ (both verified), so $\hat{\rho}_{\mathcal{H}} = \hat{\rho}_g$ and $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}}) = 0$.

**Surprisal sector (by construction, trivial; normalization uses the weighted condition $\int u\,Q\sqrt{\vert g\vert}\,d^3x = 0$).** The gated state is the constant Neumann mode, $\rho_{\mathrm{local}} = \vert\phi_0\rangle\langle\phi_0\vert$, so $Q$ is uniform, $\nabla q = 0$, $\partial_\tau\mathcal{H} = J_E^\lambda\nabla_\lambda q = 0$, and $\mathcal{H} = \mathcal{H}_0$. The reference prior is inherited from §5.4: $P = Q(1 + \epsilon(\tau)u)$ with $\int u\,z^{\sqrt{2}}\,d^3x = 0$ (the weighted condition, since $Q$ is uniform and $\sqrt{\vert g\vert} = z^{\sqrt{2}}$), $\vert u\vert < 1$, $u \not\equiv 0$, and $\epsilon(\tau) \in (0,1)$ decreasing to $0$, so $D_{\mathrm{KL}}(Q \parallel P) > 0$ ($\dot{W}_{\mathrm{var}} > 0$) and $V_Q/V_P \to 1$. Declare $\Psi = \int_{\mathcal{M}}\mathcal{H}\,d^3x$ and the ultralocal $\mathcal{H}_{\mathrm{sol}}(g, \mathbf{x}) = \mathcal{H}_0(z)$. Then $\delta\Psi/\delta g_{\mu\nu} = 0$, $\partial\mathcal{H}_{\mathrm{sol}}/\partial g_{\mu\nu} = 0$, and $\delta\Psi/\delta\mathcal{H} \equiv 1$, so the $O_\Omega$ Eq. [2] locus condition holds, $\delta\Psi/\delta\mathcal{H} \neq 0$, and $\vert\delta\Psi/\delta\mathcal{H}\vert$ is bounded and bounded away from $0$ uniformly (derived). The Branch II generator condition $\hat{\mathbb{L}}_{\mathrm{stat}}\Psi = (J_E^\lambda\nabla_\lambda q)\,\delta\Psi/\delta\mathcal{H} = 0$ therefore holds at every $\tau$, and a fortiori asymptotically. An active, decaying surprisal sector (as in §5.10) is not constructed here.

**Relational edge (verified).** With $\Phi^{(1)} = \Phi^{(2)} = \frac{3}{4}z^2$ and $\eta_{1\to 2} = -\eta_{2\to 1} = \frac{c_J(\tau)}{1 - 1/\sqrt{2}}\partial_z$, where $c_J(\tau) = c_0e^{-\gamma_c(\tau-\tau_0)}$ ($c_0, \gamma_c > 0$) decays integrably (Branch II requires this; see Decision 6):
* $J_{[1\to 2]} = c_J(\tau)\,dz$, $J_{1\to 2} + J_{2\to 1} = 0$, and $F^{(1\to 2)} = 0$ at every $\tau$, so the curvature bracket is inactive;
* $(M^{(12)})^\mu_{\;\nu} = \gamma_Mc_J^2e^{2a}\mathrm{diag}(-\frac{1}{3}, -\frac{1}{3}, \frac{2}{3})$: trace-free and non-zero everywhere at every finite $\tau$, with the eigenvalue formula and $m_+ \neq -m_-$ verified and the signs $m_+ > 0 > m_-$ read off from it, and, since $e^{2a} \le e^{0.8}$ is bounded, $\vert M^{(12)}\vert \le \mathrm{const}\cdot c_J^2$ is integrable and tends to $0$ (derived);
* with a constant coupling amplitude, the $O_6$ flux law would make $\mathcal{I}$ grow linearly without bound, contradicting $\mathcal{I} \to s_0V_\infty$; the decaying amplitude makes $\int d\mathcal{I} < \infty$.

**Harmonic current.** $d\varphi$ ($\varphi$ the azimuth) is co-closed for $g$ at every $\tau$ (verified), because the planar block is isotropic; $c_{\mathrm{harm}}\,d\varphi$ satisfies the absolute boundary conditions of §5.11 (inherited, not checked).

**Drive (default in this witness; cone-preservation identity verified for arbitrary $a_{\mathrm{d}}$).** The witness uses the default $a_{\mathrm{d}} = 0$, so its trajectories obey the r6 geodesic equation. An arbitrary potential $\Phi_{\mathrm{d}} \in C^\infty(\mathcal{M})$ would be a non-parametric field and is not admissible under the closure; closure conditions (ii)–(v) are empirical and are not applicable to a mathematical witness. For the projected form $f^\mu_{\mathrm{drive}} = (1-u^2)(a^\mu_{\mathrm{d}} - (a_{\mathrm{d}}\cdot v)v^\mu)$ with any $a_{\mathrm{d}}$, the script verifies, for this metric and arbitrary $(\mathbf{x}, v, a_{\mathrm{d}})$, that along solutions $du^2/d\tau = (1-u^2)\big(-\partial_\tau g_{\rho\epsilon}v^\rho v^\epsilon + 2(1-u^2)\,a_{\mathrm{d}}\cdot v\big)$, so $u^2 = 1$ is invariant and $u^2 < 1$ is preserved. The right side is smooth, so trajectories exist locally and are unique.

**Inherited, not recomputed.**
* Flux positivity and geodesic convexity of the overlap $E$ (§5.12). With the $e^{3H_0\tau/2}$ factor removed from $\eta$, $M_{\mu\nu}$ is invariant under $g \to cg$; the unit normals contribute $c^{-1}$ and $dA$ contributes $c$, so the boundary flux is unchanged up to the positive factor $c_J(\tau)^2/c_0^2$, and the sign of the second fundamental form is preserved under constant rescaling. The tested ellipsoids, the range $a \in [0, 8]$, and the convexity threshold therefore carry over, but they were not re-run.
* The gauge sector and overlap divergence (§5.8), with $\hat{\chi} = \chi_E\hat{u}$ and $\chi_E$ spatially constant here.
* The Gaussian-copula $Q_{12}$ of §5.8, with initial information $\mathcal{I}(\tau_0)$ and normalization chosen so that the integrated flux, finite because $c_J$ decays integrably, brings $\mathcal{I}(\tau) \to s_0V_\infty$.

**Branch I regression (verified).** The same code, applied to the §5.11 metric with $H_0 > 0$, confirms $\theta = 3H_0$, $G = \kappa_G T^{\mathrm{mat}}$, the $\tau$-compatibility law, and the elliptic $\theta$-equation with shear. This is an independent re-implementation of the §5.11 stress-sector checks, not a re-run of `e2e_5_11.py`.

**Status after r10.**
* The generalized r7 system has at least one Branch II configuration, with each property verified, derived, or inherited as itemized above, with $\theta = 0$, $\Theta_E > 0$, curvature $G \neq 0$ with active $\kappa_G$, relaxing shear, anisotropic $\mathfrak{K}$, an interior sink $\mathcal{R}_{\mathcal{F}} > 0$, and a decaying relational coupling. Each r7 block, edited or not, was reviewed against it (including $O_0$ Eq. [0], satisfied by the rounded hollow cylinder of §5.11, whose box description above is before rounding, and $O_2$ Eq. [1], satisfied by the explicit smooth metric); $O_5$ Eq. [0] required the r7 amendment to $\ge 0$ noted above. Blocks not otherwise discussed above are, by status:
  * **Verified:** $O_3$ Eq. [2] (the damping law $\partial_\tau\sigma^\mu_{\;\nu} = -\gamma_\sigma\sigma^\mu_{\;\nu}$ for the declared $a(\tau)$).
  * **Derived:** $O_3$ Eq. [0] ($f^{\mathrm{top}} = -\nabla\Phi$ with the declared $\Phi$; $V_{\mathrm{local}}$ constant because $\mathcal{H} = \mathcal{H}_0$ is static), Eq. [1] and Eq. [3] ($\theta = 0$, the Weyl split with $\det\hat{g} = 1$, $\hat{h} \to \hat{h}_\infty$); $O_7$ Eq. [2] ($\hat{\rho}_g \to \frac{1}{3}\delta$ as $a \to a_\infty$, since $g \to G_\infty = \Omega^2\hat{g}_\infty$); $O_6$ Eq. [4] ($V_{\mathcal{M}} = V_\infty$ for all $\tau$, so the volume shares and $c_{ij}$ are constant); $O_\Omega$ Eq. [1] ($\theta = 0 = nH_0$, $\int\langle\theta\rangle = 0$, $\langle\Theta_E\rangle = \Theta_\infty > 0$, $\sigma \to 0$, and bounded Christoffel symbols and curvature on the compact domain as $a \to a_\infty$); $O_\Omega$ Eq. [2] (with $\Psi$ and $\mathcal{H}_{\mathrm{sol}}$ as declared above). In $O_7$ Eq. [3], $u_{\mathrm{exp}} = 0$, $J_E$ is static and smooth on a compact domain (so $\sup\Vert J_E\Vert_{C^1} < \infty$), and $\mathcal{L}_{\mathbf{J}_E}(\hat{h} - \hat{h}_\infty) = 0$ exactly: $\hat{h} - \hat{h}_\infty$ is diagonal with spatially constant mixed components, and $\partial_\nu J_E^\mu$ is diagonal (only its $(z,z)$ entry is non-zero), so the Lie derivative reduces to the commutator of two diagonal matrices, which vanishes.
  * **Inherited:** $O_\Omega$ Eq. [0] ($V_{\mathcal{M}} = V_\infty$ derived; $\mathcal{I} \to s_0V_\infty$ via the inherited copula).
  * **Trivial:** $O_7$ Eq. [0], since $\mathcal{A}_{\mathcal{M}} = 0$ because $\nabla q = 0$.
  * **Inherited from §5.11 with $\mathcal{U}_1 = \mathcal{M}$, $\mathcal{U}_2 = E$, and $g^{(1)} = g^{(2)} = g$:** $O_5$ Eq. [0]–[3] (cover, geometric mean, $\mathbf{C}_{\mathrm{top}}$, gluing).
  * **Inherited from §5.8:** $O_6$ Eq. [0]–[1] (joint and conditional densities, through the copula) and $O_7$ Eq. [1]'s overlap-divergence limit.
  * **Inherited, as stated above:** $O_7$ Eq. [4] (gauge sector).
  * **Default:** $O_2$ Eq. [3] ($a_{\mathrm{d}} = 0$; cone-preservation identity verified for arbitrary $a_{\mathrm{d}}$).
* Not shown: a witness, in either branch, in which the conformal-Killing term of $O_6$ Eq. [3] is non-zero ($J_{i\to j} + J_{j\to i} = 0$ in every witness) or in which $\hat{\Pi}^{(i)} \neq \hat{\Pi}^{(j)}$ (so the $O_6$ Eq. [2] distinction is never exercised); a Branch II witness with $\theta > 0$ decaying integrably ($J_{\mathrm{geom}} \neq 0$, $V_{\mathcal{M}}$ actually converging; here $\theta \equiv 0$, so $O_0$ Eq. [4] Branch II and the $O_7$ Eq. [3] flux identity are exercised only trivially), with non-zero $D_{\mathrm{KL}}(\hat{\rho}_g \parallel \hat{\rho}_{\mathcal{H}})$ or $\mathcal{A}_{\mathcal{M}}$ (both $\equiv 0$ here), with distinct subsystem metrics $g^{(1)} \neq g^{(2)}$ (here equal, so the geometric mean and gluing of $O_5$ Eq. [1]–[3] are exercised only trivially), with a gradient not aligned with an eigendirection of $\mathfrak{K}$ (here $\nabla\mathcal{F} \parallel dz$, so $k_1$ never enters; the anisotropy exercised is $\mathfrak{K} \not\propto g^{-1}$, not $k_1 \neq k_3$), with an active surprisal sector (permitted by r7, which states the Branch II generator condition asymptotically), a non-zero curvature bracket, a non-trivial $f_{\mathrm{drive}}$ with verified trajectory properties, or a spatially varying sink. These remain open.
