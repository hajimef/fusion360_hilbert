import adsk.core, adsk.fusion, adsk.cam, traceback, math
from .simplelogo import SimpleLogo

app = adsk.core.Application.get()
if app:
    ui = app.userInterface
    product = app.activeProduct
design = adsk.fusion.Design.cast(product)
rootComp = design.rootComponent
sketches = rootComp.sketches
xyPlane = rootComp.xYConstructionPlane

def hilbert(logo, depth, turn, size):
    if (depth == 0):
        return
    logo.right(turn)
    hilbert(logo, depth - 1, -turn, size)
    logo.forward(size)
    logo.left(turn)
    hilbert(logo, depth - 1, turn, size)
    logo.forward(size)
    hilbert(logo, depth - 1, turn, size)
    logo.left(turn)
    logo.forward(size)
    hilbert(logo, depth - 1, -turn, size)
    logo.right(turn)

def run(context):
    try:
        s = 0.6
        sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines
        arcs = sketch.sketchCurves.sketchArcs
        logo = SimpleLogo()
        logo.lines = lines
        logo.arcs = arcs
        hilbert(logo, 4, 90, s)
        sketch2 = sketches.add(rootComp.xYConstructionPlane)
        lines2 = sketch2.sketchCurves.sketchLines
        l1 = lines2.addByTwoPoints(adsk.core.Point3D.create(0, -s / 4, 0), adsk.core.Point3D.create(0, s / 4, 0))
        l2 = lines2.addByTwoPoints(adsk.core.Point3D.create(0, s / 4, 0), adsk.core.Point3D.create(0, s / 4, s / 2))
        l3 = lines2.addByTwoPoints(adsk.core.Point3D.create(0, s / 4, s / 2), adsk.core.Point3D.create(0, -s / 4, s / 2))
        l4 = lines2.addByTwoPoints(adsk.core.Point3D.create(0, -s / 4, s / 2), adsk.core.Point3D.create(0, -s / 4, 0))
        prof = sketch2.profiles.item(0)
        path = rootComp.features.createPath(logo.paths)
        sweeps = rootComp.features.sweepFeatures
        sweepInput = sweeps.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweep = sweeps.add(sweepInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
