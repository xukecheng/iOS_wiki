Type Property

# invalidated

Displayed data should appear as invalidated and pending a new update.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let invalidated: RedactionReasons

## Discussion

Views marked with `invalidatableContent` will be automatically redacted with a
standard styling indicating the content is invalidated and new content will be
available soon.

## See Also

### Getting redaction reasons

`static let placeholder: RedactionReasons`

Displayed data should appear as generic placeholders.

`static let privacy: RedactionReasons`

Displayed data should be obscured to protect private information.

Type Property

# placeholder

Displayed data should appear as generic placeholders.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let placeholder: RedactionReasons

## Discussion

Text and images will be automatically masked to appear as generic
placeholders, though maintaining their original size and shape. Use this to
create a placeholder UI without directly exposing placeholder data to users.

## See Also

### Getting redaction reasons

`static let invalidated: RedactionReasons`

Displayed data should appear as invalidated and pending a new update.

`static let privacy: RedactionReasons`

Displayed data should be obscured to protect private information.

Type Property

# privacy

Displayed data should be obscured to protect private information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    static let privacy: RedactionReasons

## Discussion

Views marked with `privacySensitive` will be automatically redacted using a
standard styling. To apply a custom treatment the redaction reason can be read
out of the environment.

## See Also

### Getting redaction reasons

`static let invalidated: RedactionReasons`

Displayed data should appear as invalidated and pending a new update.

`static let placeholder: RedactionReasons`

Displayed data should appear as generic placeholders.

Initializer

# init(rawValue:)

Creates a new set from a raw value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(rawValue: Int)

##  Parameters

`rawValue`

    

The raw value with which to create the reasons for redaction.

## See Also

### Creating redaction reasons

`let rawValue: Int`

The raw value.

Instance Property

# rawValue

The raw value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    let rawValue: Int

## See Also

### Creating redaction reasons

`init(rawValue: Int)`

Creates a new set from a raw value.

