Type Property

# automatic

A platform-appropriate default text input dictation behavior.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static let automatic: TextInputDictationBehavior

## Discussion

The automatic behavior uses a `TextInputDictationActivation` value of `onLook`
for visionOS apps and `onSelect` for iOS apps.

## See Also

### Getting behavior values

`static func inline(activation: TextInputDictationActivation) ->
TextInputDictationBehavior`

Adds a dictation microphone in the search bar.

`static let preventDictation: TextInputDictationBehavior`

Prevents the search bar from having a dictation microphone.

Type Method

# inline(activation:)

Adds a dictation microphone in the search bar.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    static func inline(activation: TextInputDictationActivation) -> TextInputDictationBehavior

## See Also

### Getting behavior values

`static let automatic: TextInputDictationBehavior`

A platform-appropriate default text input dictation behavior.

`static let preventDictation: TextInputDictationBehavior`

Prevents the search bar from having a dictation microphone.

Type Property

# preventDictation

Prevents the search bar from having a dictation microphone.

visionOS 1.0+

    
    
    static let preventDictation: TextInputDictationBehavior

## See Also

### Getting behavior values

`static let automatic: TextInputDictationBehavior`

A platform-appropriate default text input dictation behavior.

`static func inline(activation: TextInputDictationActivation) ->
TextInputDictationBehavior`

Adds a dictation microphone in the search bar.

