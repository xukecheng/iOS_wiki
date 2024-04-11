Case

# ContentSizeCategory.extraExtraExtraLarge

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraExtraExtraLarge

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.extraExtraLarge

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraExtraLarge

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.extraLarge

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraLarge

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraSmall`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.extraSmall

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case extraSmall

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case large`

`case medium`

`case small`

Case

# ContentSizeCategory.large

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case large

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case medium`

`case small`

Case

# ContentSizeCategory.medium

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case medium

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case small`

Case

# ContentSizeCategory.small

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    case small

## See Also

### Content size categories

`case accessibilityExtraExtraExtraLarge`

`case accessibilityExtraExtraLarge`

`case accessibilityExtraLarge`

`case accessibilityLarge`

`case accessibilityMedium`

`case extraExtraExtraLarge`

`case extraExtraLarge`

`case extraLarge`

`case extraSmall`

`case large`

`case medium`

Initializer

# init(_:)

Create a size category from its UIContentSizeCategory equivalent.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    init?(_ uiSizeCategory: UIContentSizeCategory)

Instance Property

# isAccessibilityCategory

A Boolean value indicating whether the content size category is one that is
associated with accessibility.

iOS 13.4–17.4  Deprecated  iPadOS 13.4–17.4  Deprecated  macOS 10.15.4–14.4
Deprecated  Mac Catalyst 13.4–17.4  Deprecated  tvOS 13.4–17.4  Deprecated
watchOS 6.2–10.4  Deprecated  visionOS 1.0+

    
    
    var isAccessibilityCategory: Bool { get }

Operator

# <(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
less than that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func < (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool

Operator

# >(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func > (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool

Operator

# <=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
less than or equal to that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func <= (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool

Operator

# >=(_:_:)

Returns a Boolean value indicating whether the value of the first argument is
greater than or equal to that of the second argument.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func >= (lhs: ContentSizeCategory, rhs: ContentSizeCategory) -> Bool

