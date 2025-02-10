import batman
import numpy as np

# L'objet `TransitParams` de `batman` permet d'emmagasiner les paramètres de notre modèle de transit.
# Batman utilise l'inclinaison, par défaut. Dans notre cas, nous utilisons le paramètre d'impact. Il faut donc convertir entre les deux.

# Dans le devoir, t sera tiré des données.
t = np.linspace(-100, 100, num=400)

b = 0.1  # Valeur test. Paramètre à ajuster
params = batman.TransitParams()
params.t0 = 1.25  # Paramètre libre: Valeur dans l'interval de l'énoncé, pour un premier test
params.per = 3  # Paramètre fixe
params.rp = 0.05  # Paramètre libre: Valeur dans l'interval de l'énoncé, pour un premier test
params.a = 15  # Paramètre fixe: demi-grand axe, en unités de Rstar
params.inc = ___  # TODO: convertir impact -> Inc
params.ecc = 0.0  # Paramètre fixe: Orbite circulaire
params.w = 90.0  # Paramètre fixe: Orbite circulaire [w en degrés]
params.limb_dark = "quadratic"
params.u = [0.3, 0.3]  # Paramètre fixe: Coefficients pour le "limb darkening"

transit_model = batman.TransitModel(params, t)

flux_model = transit_model.light_curve(params)
