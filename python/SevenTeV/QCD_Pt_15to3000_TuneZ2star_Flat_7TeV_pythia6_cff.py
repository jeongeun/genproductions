import FWCore.ParameterSet.Config as cms

pythiaUESettingsBlock = cms.PSet(
        pythiaUESettings = cms.vstring(
                'MSTU(21)=1     ! Check on possible errors during program execution',
                'MSTJ(22)=2     ! Decay those unstable particles',
                'PARJ(71)=10 .  ! for which ctau  10 mm',
                'MSTP(33)=0     ! no K factors in hard cross sections',
                'MSTP(2)=1      ! which order running alphaS',
                'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
                'MSTP(52)=2     ! work with LHAPDF',

                'PARP(82)=1.921 ! pt cutoff for multiparton interactions',
                'PARP(89)=1800. ! sqrts for which PARP82 is set',
                'PARP(90)=0.227 ! Multiple interactions: rescaling power',

                'MSTP(95)=6     ! CR (color reconnection parameters)',
                'PARP(77)=1.016 ! CR',
                'PARP(78)=0.538 ! CR',

                'PARP(80)=0.1   ! Prob. colored parton from BBR',

                'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
                'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',

                'PARP(62)=1.025 ! ISR cutoff',

                'MSTP(91)=1     ! Gaussian primordial kT',
                'PARP(93)=10.0  ! primordial kT-max',

                'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
                'MSTP(82)=4     ! Defines the multi-parton model',
        )
)

generator = cms.EDFilter('Pythia6GeneratorFilter',
	comEnergy = cms.double(7000.0),
	crossSection = cms.untracked.double(2.212682e+10),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(0),

	PythiaParameters = cms.PSet(
		pythiaUESettingsBlock,
		processParameters = cms.vstring(
			'MSEL = 1        ! QCD hight pT processes',
			'CKIN(3) = 15    ! minimum pt hat for hard interactions',
			'CKIN(4) = 3000  ! maximum pt hat for hard interactions',
			'MSTP(142) = 2   ! Turns on the PYWEVT Pt reweighting routine',
		),
		CSAParameters = cms.vstring(
			'CSAMODE = 7     ! towards a flat QCD spectrum',
			'PTPOWER = 4.5   ! reweighting of the pt spectrum',
		),
		parameterSets = cms.vstring(
			'pythiaUESettings',
			'processParameters',
			'CSAParameters',
		)
	)
)

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('\$Revision: 1.9 $'),
	name = cms.untracked.string('\$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/Attic/QCD_Pt_15to3000_TuneZ2star_Flat_7TeV_pythia6_cff.py,v $'),
	annotation = cms.untracked.string('Summer2011 sample with PYTHIA6: QCD dijet production, pThat = 15 .. 3000 GeV, weighted, TuneZ2star')
)
