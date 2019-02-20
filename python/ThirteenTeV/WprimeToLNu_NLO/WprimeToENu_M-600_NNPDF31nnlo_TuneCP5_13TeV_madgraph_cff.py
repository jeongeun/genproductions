import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/j/jelee/public/tarballs/WprimeToENu/WprimeToENu_M-600_NLO_NNPDF31nnlo_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(20000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

###Included for 2018
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'PDF:pSet = LHAPDF6:NNPDF31_nnlo_as_0118_nf_4',
            'NewGaugeBoson:ffbar2Wprime = on',
            '34:m0 = 600',
            '34:onMode = off',
            '34:onIfAny = 11,12',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8PSweightsSettings',
                                    'pythia8CP5Settings',
                                    )
    )
)

ProductionFilterSequence = cms.Sequence(generator)
