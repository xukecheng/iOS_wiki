Type Property

# large

The system detent for a sheet at full height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let large: PresentationDetent

## See Also

### Getting built-in detents

`static let medium: PresentationDetent`

The system detent for a sheet that’s approximately half the height of the
screen, and is inactive in compact height.

Type Property

# medium

The system detent for a sheet that’s approximately half the height of the
screen, and is inactive in compact height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static let medium: PresentationDetent

## See Also

### Getting built-in detents

`static let large: PresentationDetent`

The system detent for a sheet at full height.

Type Method

# custom(_:)

A custom detent with a calculated height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func custom<D>(_ type: D.Type) -> PresentationDetent where D : CustomPresentationDetent

## See Also

### Creating custom detents

`static func fraction(CGFloat) -> PresentationDetent`

A custom detent with the specified fractional height.

`static func height(CGFloat) -> PresentationDetent`

A custom detent with the specified height.

`struct Context`

Information that you use to calculate the presentation’s height.

Type Method

# fraction(_:)

A custom detent with the specified fractional height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func fraction(_ fraction: CGFloat) -> PresentationDetent

## See Also

### Creating custom detents

`static func custom<D>(D.Type) -> PresentationDetent`

A custom detent with a calculated height.

`static func height(CGFloat) -> PresentationDetent`

A custom detent with the specified height.

`struct Context`

Information that you use to calculate the presentation’s height.

Type Method

# height(_:)

A custom detent with the specified height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static func height(_ height: CGFloat) -> PresentationDetent

## See Also

### Creating custom detents

`static func custom<D>(D.Type) -> PresentationDetent`

A custom detent with a calculated height.

`static func fraction(CGFloat) -> PresentationDetent`

A custom detent with the specified fractional height.

`struct Context`

Information that you use to calculate the presentation’s height.

Structure

# PresentationDetent.Context

Information that you use to calculate the presentation’s height.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @dynamicMemberLookup
    struct Context

## Topics

### Getting the height

`var maxDetentValue: CGFloat`

The height that the presentation appears in.

### Supporting types

`subscript<T>(dynamicMember _: KeyPath<EnvironmentValues, T>) -> T`

Returns the value specified by the keyPath from the environment.

## See Also

### Creating custom detents

`static func custom<D>(D.Type) -> PresentationDetent`

A custom detent with a calculated height.

`static func fraction(CGFloat) -> PresentationDetent`

A custom detent with the specified fractional height.

`static func height(CGFloat) -> PresentationDetent`

A custom detent with the specified height.

