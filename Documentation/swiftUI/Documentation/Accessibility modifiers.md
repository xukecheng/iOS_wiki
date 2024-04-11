Instance Method

# speechAdjustedPitch(_:)

Raises or lowers the pitch of spoken text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAdjustedPitch(_ value: Double) -> some View
    

##  Parameters

`value`

    

The amount to raise or lower the pitch. Values between `-1` and `0` result in
a lower pitch while values between `0` and `1` result in a higher pitch. The
method clamps values to the range `-1` to `1`.

## Discussion

Use this modifier when you want to change the pitch of spoken text. The value
indicates how much higher or lower to change the pitch.

## See Also

### Configuring VoiceOver

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAlwaysIncludesPunctuation(_:)

Sets whether VoiceOver should always speak all punctuation in the text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAlwaysIncludesPunctuation(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that you set to `true` if VoiceOver should speak all
punctuation in the text. Defaults to `true`.

## Discussion

Use this modifier to control whether the system speaks punctuation characters
in the text. You might use this for code or other text where the punctuation
is relevant, or where you want VoiceOver to speak a verbatim transcription of
the text you provide. For example, given the text:

VoiceOver would speak “All the world apostrophe s a stage comma and all the
men and women merely players semicolon”.

By default, VoiceOver voices punctuation based on surrounding context.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAnnouncementsQueued(_:)

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAnnouncementsQueued(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that determines if VoiceOver speaks changes to text
immediately or enqueues them behind existing speech. Defaults to `true`.

## Discussion

Use this modifier when you want affect the order in which the accessibility
system delivers spoken text. Announcements can occur automatically when the
label or value of an accessibility element changes.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechSpellsOutCharacters(Bool) -> some View`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechSpellsOutCharacters(_:)

Sets whether VoiceOver should speak the contents of the text view character by
character.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechSpellsOutCharacters(_ value: Bool = true) -> some View
    

##  Parameters

`value`

    

A Boolean value that when `true` indicates VoiceOver should speak text as
individual characters. Defaults to `true`.

## Discussion

Use this modifier when you want VoiceOver to speak text as individual letters,
character by character. This is important for text that is not meant to be
spoken together, like:

  * An acronym that isn’t a word, like APPL, spoken as “A-P-P-L”.

  * A number representing a series of digits, like 25, spoken as “two-five” rather than “twenty-five”.

## See Also

### Configuring VoiceOver

`func speechAdjustedPitch(Double) -> some View`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> some View`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> some View`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

