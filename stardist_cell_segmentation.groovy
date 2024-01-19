import static qupath.lib.gui.scripting.QPEx.*
import qupath.lib.gui.dialogs.Dialogs
def pathModel = buildFilePath(QPEx.PROJECT_BASE_DIR, "\\stardist_cell_seg_model.pb")

import qupath.ext.stardist.StarDist2D

def stardist = StarDist2D.builder(pathModel)
        .threshold(0.5)                     // Probability (detection) threshold
        .channels(0)                        // Select detection channel
        .normalizePercentiles(0.01, 99.99)  // Percentile normalization
        .pixelSize(0.5)                     // Resolution for detection
        .cellExpansion(1.0)                 // Approximate cells based upon nucleus expansion
        .cellConstrainScale(0.5)            // Constrain cell expansion using nucleus size
        .measureShape()                     // Add shape measurements
        .measureIntensity()                 // Add cell measurements (in all compartments)
        .includeProbability(true)           // Add probability as a measurement (enables later filtering)
        .build()

// Run detection for the selected objects


def imageData = getCurrentImageData()
def server = imageData.getServer()
createSelectAllObject(true)
def pathObjects = getSelectedObjects()
if (pathObjects.isEmpty()) {
    Dialogs.showErrorMessage("StarDist", "Please select a parent object!")
    return
}
stardist.detectObjects(imageData, pathObjects)
println 'Detection done!'

def fileName = server.getMetadata().getName()
def pathOutput = buildFilePath(QPEx.PROJECT_BASE_DIR, 'json')
mkdirs(pathOutput)
exportAllObjectsToGeoJson(pathOutput + "\\" + fileName[0..-5] + ".geojson", "EXCLUDE_MEASUREMENTS", "PRETTY_JSON", "FEATURE_COLLECTION")
println 'json saved!'
