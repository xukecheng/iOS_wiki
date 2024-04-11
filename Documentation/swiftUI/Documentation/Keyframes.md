Instance Property

# body

The composition of content that comprise the keyframes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @KeyframesBuilder<Self.Value> var body: Self.Body { get }

**Required**

## See Also

### Creating a keyframe

`associatedtype Body : Keyframes`

The type of keyframes representing the body of this type.

**Required**

` associatedtype Value = Self.Body.Value`

The type of value animated by this keyframes type

**Required**

Associated Type

# Body

The type of keyframes representing the body of this type.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Body : Keyframes

**Required**

## Discussion

When you create a custom keyframes type, Swift infers this type from your
implementation of the required `body` property.

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframes.

**Required**

` associatedtype Value = Self.Body.Value`

The type of value animated by this keyframes type

**Required**

Associated Type

# Value

The type of value animated by this keyframes type

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Value = Self.Body.Value

**Required**

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframes.

**Required**

` associatedtype Body : Keyframes`

The type of keyframes representing the body of this type.

**Required**

