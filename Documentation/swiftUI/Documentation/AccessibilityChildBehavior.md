Type Property

# combine

Any child accessibility element’s properties are merged into the new
accessibility element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let combine: AccessibilityChildBehavior

## Discussion

Use this behavior when you want a view represented by a single accessibility
element. The new accessibility element merges properties from all non-hidden
children. Some properties may be transformed or ignored to achieve the ideal
combined result. For example, not all of `AccessibilityTraits` are merged and
a `default` action may become a named action (`init(named:)`).

A new accessibility element is created when:

  * The view contains multiple or zero accessibility elements

  * The view wraps a `UIViewRepresentable`/`NSViewRepresentable`.

Note

If an accessibility element is not created, the `AccessibilityChildBehavior`
of the existing accessibility element is modified.

## See Also

### Getting behaviors

`static let contain: AccessibilityChildBehavior`

Any child accessibility elements become children of the new accessibility
element.

`static let ignore: AccessibilityChildBehavior`

Any child accessibility elements become hidden.

Type Property

# contain

Any child accessibility elements become children of the new accessibility
element.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let contain: AccessibilityChildBehavior

## Discussion

Use this behavior when you want a view to be an accessibility container. An
accessibility container groups child accessibility elements which improves
navigation. For example, all children of an accessibility container are
navigated in order before navigating through the next accessibility container.

A new accessibility element is created when:

  * The view contains multiple or zero accessibility elements

  * The view contains a single accessibility element with no children

Note

If an accessibility element is not created, the `AccessibilityChildBehavior`
of the existing accessibility element is modified.

## See Also

### Getting behaviors

`static let combine: AccessibilityChildBehavior`

Any child accessibility element’s properties are merged into the new
accessibility element.

`static let ignore: AccessibilityChildBehavior`

Any child accessibility elements become hidden.

Type Property

# ignore

Any child accessibility elements become hidden.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static let ignore: AccessibilityChildBehavior

## Discussion

Use this behavior when you want a view represented by a single accessibility
element. The new accessibility element has no initial properties. So you will
need to use other accessibility modifiers, such as `accessibilityLabel(_:)`,
to begin making it accessible.

Before using the `ignore`behavior, consider using the `combine` behavior.

Note

A new accessibility element is always created.

## See Also

### Getting behaviors

`static let combine: AccessibilityChildBehavior`

Any child accessibility element’s properties are merged into the new
accessibility element.

`static let contain: AccessibilityChildBehavior`

Any child accessibility elements become children of the new accessibility
element.

