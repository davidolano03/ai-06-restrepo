import AR18RaceManMachine.MainTheorems
/-! Partial support contracts, NOT full source theorem specifications.
The equations below are explicit proof-level premises. Their derivation from
primitive task technology, equilibrium and differentiation remains open.
All original named source results remain unformalized in this checkpoint. -/
namespace AR18RaceManMachine

def StaticResponseAlgebraSpec : Prop :=
  ∀ s σ ε g z w r ell : ℝ, σ + ε ≠ 0 →
    σ * (w - r) + ell = z → ell = ε * (w - r) →
    s * w + (1 - s) * r = g →
    w = g + (1 - s) * (z / (σ + ε)) ∧
    r = g - s * (z / (σ + ε)) ∧ ell = ε * (z / (σ + ε))

def StaticResponseExistenceSpec : Prop :=
  ∀ s σ ε g z : ℝ, σ + ε ≠ 0 →
    ∃ w r ell : ℝ, σ * (w - r) + ell = z ∧
      ell = ε * (w - r) ∧ s * w + (1 - s) * r = g

def WageDeclinePossibleAlgebraSpec : Prop :=
  ∀ s σ ε Λ : ℝ, s < 1 → 0 < σ → 0 < ε → 0 < Λ →
    ∃ g : ℝ, 0 < g ∧ g - (1 - s) * (Λ / (σ + ε)) < 0

end AR18RaceManMachine
