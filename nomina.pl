% Declaración de predicados dinámicos
:- dynamic profesor/3.

% Datos de ejemplo
profesor(ana_garcia, auxiliar, 3200000).
profesor(pedro_lopez, asociado, 5200000).
profesor(luisa_martinez, titular, 7500000).

% Deducciones
deduccion_salud(SalarioBase, DeduccionSalud) :-
    DeduccionSalud is SalarioBase * 0.03.

deduccion_pension(SalarioBase, DeduccionPension) :-
    DeduccionPension is SalarioBase * 0.05.

% Bonificaciones
bonificacion(auxiliar, SalarioBase, Bonificacion) :-
    Bonificacion is SalarioBase * 0.06.
bonificacion(asociado, SalarioBase, Bonificacion) :-
    Bonificacion is SalarioBase * 0.12.
bonificacion(titular, SalarioBase, Bonificacion) :-
    Bonificacion is SalarioBase * 0.18.

% Cálculo del salario neto
salario_neto(NombreProfesor, SalarioNeto) :-
    profesor(NombreProfesor, Categoria, SalarioBase),
    deduccion_salud(SalarioBase, DeduccionSalud),
    deduccion_pension(SalarioBase, DeduccionPension),
    bonificacion(Categoria, SalarioBase, Bonificacion),
    SalarioNeto is SalarioBase - DeduccionSalud - DeduccionPension + Bonificacion.
