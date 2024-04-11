Initializer

# init(function:arguments:)

Creates a new shader from a function and the uniform argument values to bind
to the function.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    init(
        function: ShaderFunction,
        arguments: [Shader.Argument]
    )

## See Also

### Creating a shader

`struct Argument`

A single uniform argument value to a shader function.

Structure

# Shader.Argument

A single uniform argument value to a shader function.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    struct Argument

## Topics

### Creating argument values

`static var boundingRect: Shader.Argument`

Returns an argument value representing the bounding rect of the shape or view
that the shader is attached to, as `float4(x, y, width, height)`. This value
is undefined for shaders that do not have a natural bounding rect (e.g. filter
effects drawn into `GraphicsContext`).

`static func color(Color) -> Shader.Argument`

Returns an argument value representing `color`. When passed to a MSL function
it will convert to a `half4` value, as a premultiplied color in the target
color space.

`static func colorArray([Color]) -> Shader.Argument`

Returns an argument value defined by the provided array of color values. When
passed to an MSL function it will convert to a `device const half4 *ptr, int
count` pair of parameters.

`static func data(Data) -> Shader.Argument`

Returns an argument value defined by the provided data value. When passed to
an MSL function it will convert to a `device const void *ptr, int
size_in_bytes` pair of parameters.

`static func float<T>(T) -> Shader.Argument`

Returns an argument value representing the MSL value `float(x)`.

`static func float2(CGVector) -> Shader.Argument`

Returns an argument value representing the MSL value `float2(vector.dx,
vector.dy)`.

`static func float2(CGPoint) -> Shader.Argument`

Returns an argument value representing the MSL value `float2(point.x,
point.y)`.

`static func float2(CGSize) -> Shader.Argument`

Returns an argument value representing the MSL value `float2(size.width,
size.height)`.

`static func float2<T>(T, T) -> Shader.Argument`

Returns an argument value representing the MSL value `float2(x, y)`.

`static func float3<T>(T, T, T) -> Shader.Argument`

Returns an argument value representing the MSL value `float3(x, y, z)`.

`static func float4<T>(T, T, T, T) -> Shader.Argument`

Returns an argument value representing the MSL value `float4(x, y, z, w)`.

`static func floatArray([Float]) -> Shader.Argument`

Returns an argument value defined by the provided array of floating point
numbers. When passed to an MSL function it will convert to a `device const
float *ptr, int count` pair of parameters.

`static func image(Image) -> Shader.Argument`

Returns an argument value defined by the provided image. When passed to an MSL
function it will convert to a `texture2d<half>` value. Currently only one
image parameter is supported per `Shader` instance.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Creating a shader

`init(function: ShaderFunction, arguments: [Shader.Argument])`

Creates a new shader from a function and the uniform argument values to bind
to the function.

Instance Property

# function

The shader function called by the shader.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var function: ShaderFunction

## See Also

### Getting the shader function

`var arguments: [Shader.Argument]`

The uniform argument values passed to the shader function.

Instance Property

# arguments

The uniform argument values passed to the shader function.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var arguments: [Shader.Argument]

## See Also

### Getting the shader function

`var function: ShaderFunction`

The shader function called by the shader.

Instance Property

# dithersColor

For shader functions that return color values, whether the returned color has
dither noise added to it, or is simply rounded to the output bit-depth. For
shaders generating smooth gradients, dithering is usually necessary to prevent
visible banding in the result.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    var dithersColor: Bool { get set }

