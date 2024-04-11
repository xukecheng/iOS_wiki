Instance Property

# body

The composition of content that comprise the keyframe track.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @KeyframeTrackContentBuilder<Self.Value> var body: Self.Body { get }

**Required**

## See Also

### Creating a keyframe

`associatedtype Body : KeyframeTrackContent`

**Required**

` associatedtype Value : Animatable = Self.Body.Value`

**Required**

Associated Type

# Body

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Body : KeyframeTrackContent

**Required**

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframe track.

**Required**

` associatedtype Value : Animatable = Self.Body.Value`

**Required**

Associated Type

# Value

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    associatedtype Value : Animatable = Self.Body.Value

**Required**

## See Also

### Creating a keyframe

`var body: Self.Body`

The composition of content that comprise the keyframe track.

**Required**

` associatedtype Body : KeyframeTrackContent`

**Required**

