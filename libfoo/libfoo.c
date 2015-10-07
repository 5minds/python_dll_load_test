// libfoo.cpp : Defines the exported functions for the DLL application.
//

#include "libfoo.h"


// This is an example of an exported variable
LIBFOO_API int nlibfoo=0;

// This is an example of an exported function.
LIBFOO_API int fnlibfoo(void)
{
	return 42;
}

