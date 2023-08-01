import asyncio
import roberto_util as util
MINIMUM_BRAWNDO_VERSION = 240
util.setup(MINIMUM_BRAWNDO_VERSION)

# Run main badge tasks
asyncio.run(util.main())