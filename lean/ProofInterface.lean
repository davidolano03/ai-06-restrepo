import AR18RaceManMachine.PaperInterface
namespace AR18RaceManMachine
 theorem staticResponseAlgebra : StaticResponseAlgebraSpec := solve_linearized_system
 theorem staticResponseExistence : StaticResponseExistenceSpec := linearized_solution_exists
 theorem wageDeclinePossibleAlgebra : WageDeclinePossibleAlgebraSpec :=
  positive_productivity_falling_wage
end AR18RaceManMachine
