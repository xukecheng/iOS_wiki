Type Property

# automatic

Automatic language behavior.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static let automatic: TypesettingLanguage

## Discussion

When determining the language to use for typesetting the current UI language
and preferred languages will be considiered. For example, if the current UI
locale is for English and Thai is included in the preferred languages then
line heights will be taller to accommodate the taller glyphs used by Thai.

## See Also

### Getting language behavior

`static func explicit(Locale.Language) -> TypesettingLanguage`

Use explicit language.

Type Method

# explicit(_:)

Use explicit language.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static func explicit(_ language: Locale.Language) -> TypesettingLanguage

##  Parameters

`language`

    

The language to use for typesetting.

## Return Value

A `TypesettingLanguage`.

## Discussion

An explicit language will be used for typesetting. For example, if used with
Thai language the line heights will be as tall as needed to accommodate Thai.

## See Also

### Getting language behavior

`static let automatic: TypesettingLanguage`

Automatic language behavior.

