
#include <RandomWorld.hxx>
#include <RandomWorldConfig.hxx>
#include <Exception.hxx>
#include <Simulation.hxx>

#include <iostream>
#include <cstdlib>

int main(int argc, char *argv[])
{
	try
	{	
		if(argc>2)
		{
			throw Engine::Exception("USAGE: randomWalkers [config file]");
		}		
	
		std::string fileName("config.xml");
		if(argc!=1)
		{
			fileName = argv[1];
		}
		Examples::RandomWorldConfig config;
		config.deserialize(fileName);
	
		Engine::Simulation helloWorldSim(config.getSize(), config.getNumSteps(), config.getSerializeResolution());
		Examples::RandomWorld world( config, helloWorldSim, world.useOpenMPSingleNode(config.getResultsFile()));
	
		world.initialize(argc, argv);
		world.run();
	}
	catch( std::exception & exceptionThrown )
	{
		std::cout << "exception thrown: " << exceptionThrown.what() << std::endl;
	}
	return 0;
}

