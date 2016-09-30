{

//Load FwLite
gSystem->Load("libFWCoreFWLite.so");
AutoLibraryLoader::enable();

//Load the Functions
//gSystem->Load("$CMSSW_BASE/lib/$SCRAM_ARCH/libCIARootAnalysis.so");
gROOT->ProcessLine(".L MonoHTauTau/ROOT/interactive/NtuplePlotter.cc+");
gROOT->ProcessLine(".L MonoHTauTau/ROOT/interactive/PhysicsDrawer.cc+");
gROOT->ProcessLine(".L MonoHTauTau/ROOT/interactive/Likelihood.cc+");
gROOT->ProcessLine(".L MonoHTauTau/ROOT/interactive/tdrstyle.C");

//Set plot styles
setTDRStyle();


}
