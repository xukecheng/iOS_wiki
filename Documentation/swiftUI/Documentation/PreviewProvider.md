Type Property

# previews

A collection of views to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    static var previews: Self.Previews { get }

**Required**

## Discussion

Implement a computed `previews` property to indicate the content to preview.
Xcode generates a preview for each view that you list. You can apply `View`
modifiers to the views, like you do when creating a custom view. For a
preview, you can also use various preview-specific modifiers that customize
the preview. For example, you can choose a specific device for the preview by
adding the `previewDevice(_:)` modifier:

For the full list of preview-specific modifiers, see Previews in Xcode.

## See Also

### Creating a preview

`associatedtype Previews : View`

The type to preview.

**Required**

Associated Type

# Previews

The type to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Previews : View

**Required**

## Discussion

When you create a preview, Swift infers this type from your implementation of
the required `previews` property.

## See Also

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

Type Property

# platform

The platform on which to run the provider.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    static var platform: PreviewPlatform? { get }

**Required** Default implementation provided.

## Discussion

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property to provide a
hint, and specify one of the `PreviewPlatform` values:

Xcode ignores this value unless you have a multiplatform target.

## Default Implementations

### PreviewProvider Implementations

`static var platform: PreviewPlatform?`

The platform to run the provider on.

Type Property

# previews

A collection of views to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @ViewBuilder @MainActor
    static var previews: Self.Previews { get }

**Required**

## Discussion

Implement a computed `previews` property to indicate the content to preview.
Xcode generates a preview for each view that you list. You can apply `View`
modifiers to the views, like you do when creating a custom view. For a
preview, you can also use various preview-specific modifiers that customize
the preview. For example, you can choose a specific device for the preview by
adding the `previewDevice(_:)` modifier:

For the full list of preview-specific modifiers, see Previews in Xcode.

## See Also

### Creating a preview

`associatedtype Previews : View`

The type to preview.

**Required**

Associated Type

# Previews

The type to preview.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    associatedtype Previews : View

**Required**

## Discussion

When you create a preview, Swift infers this type from your implementation of
the required `previews` property.

## See Also

### Creating a preview

`static var previews: Self.Previews`

A collection of views to preview.

**Required**

Type Property

# platform

The platform on which to run the provider.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    static var platform: PreviewPlatform? { get }

**Required** Default implementation provided.

## Discussion

Xcode infers the platform for a preview based on the currently selected
target. If you have a multiplatform target and want to suggest a particular
target for a preview, implement the `platform` computed property to provide a
hint, and specify one of the `PreviewPlatform` values:

Xcode ignores this value unless you have a multiplatform target.

## Default Implementations

### PreviewProvider Implementations

`static var platform: PreviewPlatform?`

The platform to run the provider on.

