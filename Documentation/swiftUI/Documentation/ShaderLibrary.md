Type Property

# default

The default shader library of the main (i.e. app) bundle.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static let `default`: ShaderLibrary

## See Also

### Getting the default shader library

`static func bundle(Bundle) -> ShaderLibrary`

Returns the default shader library of the specified bundle.

Type Method

# bundle(_:)

Returns the default shader library of the specified bundle.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func bundle(_ bundle: Bundle) -> ShaderLibrary

## See Also

### Getting the default shader library

`static let `default`: ShaderLibrary`

The default shader library of the main (i.e. app) bundle.

Initializer

# init(url:)

Creates a new Metal shader library from the contents of `url`, which must be
the location of precompiled Metal library. Functions compiled from the
returned library will only be cached as long as the returned library exists.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(url: URL)

## See Also

### Creating a shader library

`init(data: Data)`

Creates a new Metal shader library from `data`, which must be the contents of
precompiled Metal library. Functions compiled from the returned library will
only be cached as long as the returned library exists.

Initializer

# init(data:)

Creates a new Metal shader library from `data`, which must be the contents of
precompiled Metal library. Functions compiled from the returned library will
only be cached as long as the returned library exists.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(data: Data)

## See Also

### Creating a shader library

`init(url: URL)`

Creates a new Metal shader library from the contents of `url`, which must be
the location of precompiled Metal library. Functions compiled from the
returned library will only be cached as long as the returned library exists.

Type Subscript

# subscript(dynamicMember:)

Returns a new shader function representing the stitchable MSL function called
`name` in the default shader library.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static subscript(dynamicMember name: String) -> ShaderFunction { get }

## Overview

Typically this subscript is used implicitly via the dynamic member syntax, for
example:

let fn = ShaderLibrary.myFunction

which creates a reference to the MSL function called `myFunction()`.

Instance Subscript

# subscript(dynamicMember:)

Returns a new shader function representing the stitchable MSL function in the
library called `name`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    subscript(dynamicMember name: String) -> ShaderFunction { get }

## Overview

Typically this subscript is used implicitly via the dynamic member syntax, for
example:

let fn = ShaderLibrary.default.myFunction

which creates a reference to the MSL function called `myFunction()`.

