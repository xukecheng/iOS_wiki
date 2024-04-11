Type Property

# zero

A size proposal that contains zero in both dimensions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let zero: ProposedViewSize

## Discussion

Subviews of a custom layout return their minimum size when you propose this
value using the `dimensions(in:)` method. A custom layout should also return
its minimum size from the `sizeThatFits(proposal:subviews:cache:)` method for
this value.

## See Also

### Getting standard proposals

`static let infinity: ProposedViewSize`

A size proposal that contains infinity in both dimensions.

`static let unspecified: ProposedViewSize`

The proposed size with both dimensions left unspecified.

Type Property

# infinity

A size proposal that contains infinity in both dimensions.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let infinity: ProposedViewSize

## Discussion

Both dimensions contain `infinity` in this size proposal. Subviews of a custom
layout return their maximum size when you propose this value using the
`dimensions(in:)` method. A custom layout should also return its maximum size
from the `sizeThatFits(proposal:subviews:cache:)` method for this value.

## See Also

### Getting standard proposals

`static let zero: ProposedViewSize`

A size proposal that contains zero in both dimensions.

`static let unspecified: ProposedViewSize`

The proposed size with both dimensions left unspecified.

Type Property

# unspecified

The proposed size with both dimensions left unspecified.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let unspecified: ProposedViewSize

## Discussion

Both dimensions contain `nil` in this size proposal. Subviews of a custom
layout return their ideal size when you propose this value using the
`dimensions(in:)` method. A custom layout should also return its ideal size
from the `sizeThatFits(proposal:subviews:cache:)` method for this value.

## See Also

### Getting standard proposals

`static let zero: ProposedViewSize`

A size proposal that contains zero in both dimensions.

`static let infinity: ProposedViewSize`

A size proposal that contains infinity in both dimensions.

Initializer

# init(_:)

Creates a new proposed size from a specified size.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ size: CGSize)

##  Parameters

`size`

    

A proposed size with dimensions measured in points.

## See Also

### Creating a custom size proposal

`init(width: CGFloat?, height: CGFloat?)`

Creates a new proposed size using the specified width and height.

Initializer

# init(width:height:)

Creates a new proposed size using the specified width and height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        width: CGFloat?,
        height: CGFloat?
    )

##  Parameters

`width`

    

A proposed width in points. Use a value of `nil` to indicate that the width is
unspecified for this proposal.

`height`

    

A proposed height in points. Use a value of `nil` to indicate that the height
is unspecified for this proposal.

## See Also

### Creating a custom size proposal

`init(CGSize)`

Creates a new proposed size from a specified size.

Instance Property

# height

The proposed vertical size measured in points.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var height: CGFloat?

## Discussion

A value of `nil` represents an unspecified height proposal, which a view
interprets to mean that it should use its ideal height.

## See Also

### Getting the proposal’s dimensions

`var width: CGFloat?`

The proposed horizontal size measured in points.

Instance Property

# width

The proposed horizontal size measured in points.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var width: CGFloat?

## Discussion

A value of `nil` represents an unspecified width proposal, which a view
interprets to mean that it should use its ideal width.

## See Also

### Getting the proposal’s dimensions

`var height: CGFloat?`

The proposed vertical size measured in points.

Instance Method

# replacingUnspecifiedDimensions(by:)

Creates a new proposal that replaces unspecified dimensions in this proposal
with the corresponding dimension of the specified size.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func replacingUnspecifiedDimensions(by size: CGSize = CGSize(width: 10, height: 10)) -> CGSize

##  Parameters

`size`

    

A set of concrete values to use for the size proposal in place of any
unspecified dimensions. The default value is `10` for both dimensions.

## Return Value

A new, fully specified size proposal.

## Discussion

Use the default value to prevent a flexible view from disappearing into a
zero-sized frame, and ensure the unspecified value remains visible during
debugging.

