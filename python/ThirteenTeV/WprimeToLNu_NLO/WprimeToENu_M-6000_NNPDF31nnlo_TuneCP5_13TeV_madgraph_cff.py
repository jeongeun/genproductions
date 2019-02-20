import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/x3/cms/jelee/MCProd/mg26X/gridpacks/WprimeToENu_M6000_NLO_NNPDF31nnlo_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(20000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
#from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *

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
       # pythia8aMCatNLOSettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'PDF:pSet = LHAPDF6:NNPDF31_nnlo_as_0118_nf_4',
            'NewGaugeBoson:ffbar2Wprime = on',
            '34:m0 = 6000',
            '34:onMode = off',
            '34:onIfAny = 11,12',
            # 2018
            #'JetMatching:setMad = off',
            #'JetMatching:scheme = 1',
            #'JetMatching:merge = on',
            #'JetMatching:jetAlgorithm = 2',
            #'JetMatching:etaJetMax = 999.',
            #'JetMatching:coneRadius = 1.',
            #'JetMatching:slowJetPower = 1',
            #'JetMatching:qCut = 30.', #this is the actual merging scale
            #'JetMatching:doFxFx = on',
            #'JetMatching:qCutME = 10.',#this must match the ptj cut in the lhe generation step
            #'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            #'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
            #'TimeShower:mMaxGamma = 4.0',

            ##PSweights

            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    #'pythia8aMCatNLOSettings',
                                    'pythia8PSweightsSettings',
                                    'pythia8CP5Settings',
                                    )
    )
)

ProductionFilterSequence = cms.Sequence(generator)
