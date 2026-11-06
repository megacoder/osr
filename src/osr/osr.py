#!/usr/bin/env python3
# vim: ai sm noet sw=8 sw=8 nobomb ff=unix

import	os
import	sys
import  shlex

names=dict()

for line in open( "/etc/os-release" ):
    tokens = line.strip().split( "=", 1 )
    if len( tokens ) == 2:
        name = tokens[ 0 ]
        value = tokens[ 1 ]
        # print( f".. name={name}, value={value}" )
        names[ name ] = value

max_key = max(
        map(
            len,
            names
        )
)

argc = len( sys.argv )

if argc == 1:
    for key in sorted( names ):
        print( f"{key:>{max_key}}", end = "  " )
        print( f"{names[key]}" )
else:
    multi = (argc > 2)
    for key in sys.argv[ 1: ]:
        value = names.get( key.upper(), "N/A" )
        if multi:
            print( f"{key:>{max_key}}", end = "  " )
        print( value )

exit( 0 )
