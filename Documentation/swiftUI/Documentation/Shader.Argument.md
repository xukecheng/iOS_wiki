Type Property

# boundingRect

Returns an argument value representing the bounding rect of the shape or view
that the shader is attached to, as `float4(x, y, width, height)`. This value
is undefined for shaders that do not have a natural bounding rect (e.g. filter
effects drawn into `GraphicsContext`).

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static var boundingRect: Shader.Argument { get }

## See Also

### Creating argument values

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

Type Method

# color(_:)

Returns an argument value representing `color`. When passed to a MSL function
it will convert to a `half4` value, as a premultiplied color in the target
color space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func color(_ color: Color) -> Shader.Argument

## See Also

### Creating argument values

`static var boundingRect: Shader.Argument`

Returns an argument value representing the bounding rect of the shape or view
that the shader is attached to, as `float4(x, y, width, height)`. This value
is undefined for shaders that do not have a natural bounding rect (e.g. filter
effects drawn into `GraphicsContext`).

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

Type Method

# colorArray(_:)

Returns an argument value defined by the provided array of color values. When
passed to an MSL function it will convert to a `device const half4 *ptr, int
count` pair of parameters.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func colorArray(_ array: [Color]) -> Shader.Argument

## See Also

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

Type Method

# data(_:)

Returns an argument value defined by the provided data value. When passed to
an MSL function it will convert to a `device const void *ptr, int
size_in_bytes` pair of parameters.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func data(_ data: Data) -> Shader.Argument

## See Also

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

Type Method

# float(_:)

Returns an argument value representing the MSL value `float(x)`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func float<T>(_ x: T) -> Shader.Argument where T : BinaryFloatingPoint

## See Also

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

Type Method

# float2(_:)

Returns an argument value representing the MSL value `float2(vector.dx,
vector.dy)`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func float2(_ vector: CGVector) -> Shader.Argument

## See Also

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

Type Method

# float2(_:)

Returns an argument value representing the MSL value `float2(point.x,
point.y)`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func float2(_ point: CGPoint) -> Shader.Argument

## See Also

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

Type Method

# float2(_:)

Returns an argument value representing the MSL value `float2(size.width,
size.height)`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func float2(_ size: CGSize) -> Shader.Argument

## See Also

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

Type Method

# float2(_:_:)

Returns an argument value representing the MSL value `float2(x, y)`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func float2<T>(
        _ x: T,
        _ y: T
    ) -> Shader.Argument where T : BinaryFloatingPoint

## See Also

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

Type Method

# float3(_:_:_:)

Returns an argument value representing the MSL value `float3(x, y, z)`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func float3<T>(
        _ x: T,
        _ y: T,
        _ z: T
    ) -> Shader.Argument where T : BinaryFloatingPoint

## See Also

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

Type Method

# float4(_:_:_:_:)

Returns an argument value representing the MSL value `float4(x, y, z, w)`.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func float4<T>(
        _ x: T,
        _ y: T,
        _ z: T,
        _ w: T
    ) -> Shader.Argument where T : BinaryFloatingPoint

## See Also

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

`static func floatArray([Float]) -> Shader.Argument`

Returns an argument value defined by the provided array of floating point
numbers. When passed to an MSL function it will convert to a `device const
float *ptr, int count` pair of parameters.

`static func image(Image) -> Shader.Argument`

Returns an argument value defined by the provided image. When passed to an MSL
function it will convert to a `texture2d<half>` value. Currently only one
image parameter is supported per `Shader` instance.

Type Method

# floatArray(_:)

Returns an argument value defined by the provided array of floating point
numbers. When passed to an MSL function it will convert to a `device const
float *ptr, int count` pair of parameters.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func floatArray(_ array: [Float]) -> Shader.Argument

## See Also

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

`static func image(Image) -> Shader.Argument`

Returns an argument value defined by the provided image. When passed to an MSL
function it will convert to a `texture2d<half>` value. Currently only one
image parameter is supported per `Shader` instance.

Type Method

# image(_:)

Returns an argument value defined by the provided image. When passed to an MSL
function it will convert to a `texture2d<half>` value. Currently only one
image parameter is supported per `Shader` instance.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  visionOS
1.0+

    
    
    static func image(_ image: Image) -> Shader.Argument

## See Also

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

