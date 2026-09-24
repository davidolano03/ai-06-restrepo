import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-! Conditional algebra supporting NBER22252 June2017, Proposition3 and B9-B10.
The derivation of these linearized equations from the task economy is OPEN.
These are support-only results: no source theorem coverage is claimed. -/
namespace AR18RaceManMachine

theorem solve_linearized_system
    (s σ ε g z w r ell : ℝ) (hden : σ + ε ≠ 0)
    (hdemand : σ * (w - r) + ell = z)
    (hsupply : ell = ε * (w - r))
    (haccount : s * w + (1 - s) * r = g) :
    w = g + (1 - s) * (z / (σ + ε)) ∧
    r = g - s * (z / (σ + ε)) ∧ ell = ε * (z / (σ + ε)) := by
  have hrel : w - r = z / (σ + ε) := by
    apply (eq_div_iff hden).2
    nlinarith [hdemand, hsupply]
  constructor
  · rw [← hrel]
    nlinarith [haccount]
  constructor
  · rw [← hrel]
    nlinarith [haccount]
  · rw [hsupply, hrel]

/-- Nonvacuity of the reduced system, NOT of the original task economy. -/
theorem linearized_solution_exists
    (s σ ε g z : ℝ) (hden : σ + ε ≠ 0) :
    ∃ w r ell : ℝ, σ * (w - r) + ell = z ∧
      ell = ε * (w - r) ∧ s * w + (1 - s) * r = g := by
  refine ⟨g + (1 - s) * (z / (σ + ε)),
    g - s * (z / (σ + ε)), ε * (z / (σ + ε)), ?_, ?_, ?_⟩
  · field_simp
    nlinarith
  · ring
  · ring

/-- Positive productivity and wage decline are possible in response coordinates.
This does not construct a feasible nonlinear equilibrium. -/
theorem positive_productivity_falling_wage
    (s σ ε Λ : ℝ) (hs1 : s < 1) (hσ : 0 < σ)
    (hε : 0 < ε) (hΛ : 0 < Λ) :
    ∃ g : ℝ, 0 < g ∧ g - (1 - s) * (Λ / (σ + ε)) < 0 := by
  have ht : 0 < (1 - s) * (Λ / (σ + ε)) :=
    mul_pos (sub_pos.mpr hs1) (div_pos hΛ (add_pos hσ hε))
  refine ⟨((1 - s) * (Λ / (σ + ε))) / 2, ?_, ?_⟩ <;> linarith

end AR18RaceManMachine

