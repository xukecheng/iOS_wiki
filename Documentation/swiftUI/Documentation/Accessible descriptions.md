Enumeration

# AccessibilityLabeledPairRole

The role of an accessibility element in a label / content pair.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    enum AccessibilityLabeledPairRole

## Topics

### Getting roles

`case content`

This element represents the content part of the label / content pair.

`case label`

This element represents the label part of the label / content pair.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Applying labels

`func accessibilityLabel<S>(S) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(Text) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityLabel(LocalizedStringKey) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds a label to the view that describes its contents.

`func accessibilityInputLabels([LocalizedStringKey]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels<S>([S]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityInputLabels([Text]) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets alternate input labels with which users identify a view.

`func accessibilityLabeledPair<ID>(role: AccessibilityLabeledPairRole, id: ID,
in: Namespace.ID) -> some View`

Pairs an accessibility element representing a label with the element for the
matching content.

Enumeration

# AccessibilityHeadingLevel

The hierarchy of a heading in relation other headings.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum AccessibilityHeadingLevel

## Overview

Assistive technologies can use this to improve a users navigation through
multiple headings. When users navigate through top level headings they expect
the content for each heading to be unrelated.

For example, you can categorize a list of available products into sections,
like Fruits and Vegetables. With only top level headings, this list requires
no heading hierarchy, and you use the `AccessibilityHeadingLevel.unspecified`
heading level. On the other hand, if sections contain subsections, like if the
Fruits section has subsections for varieties of Apples, Pears, and so on, you
apply the `AccessibilityHeadingLevel.h1` level to Fruits and Vegetables, and
the `AccessibilityHeadingLevel.h2` level to Apples and Pears.

Except for `AccessibilityHeadingLevel.h1`, be sure to precede all leveled
headings by another heading with a level that’s one less.

## Topics

### Getting the heading level

`case h1`

Level 1 heading.

`case h2`

Level 2 heading.

`case h3`

Level 3 heading.

`case h4`

Level 4 heading.

`case h5`

Level 5 heading.

`case h6`

Level 6 heading.

`case unspecified`

A heading without a hierarchy.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Describing content

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Sets an accessibility text content type.

`func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the accessibility level of this heading.

`struct AccessibilityTextContentType`

Textual context that assistive technologies can use to improve the
presentation of spoken text.

Structure

# AccessibilityTextContentType

Textual context that assistive technologies can use to improve the
presentation of spoken text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityTextContentType

## Overview

Use an `AccessibilityTextContentType` value when setting the accessibility
text content type of a view using the `accessibilityTextContentType(_:)`
modifier.

## Topics

### Getting content types

`static let console: AccessibilityTextContentType`

A type that represents text used for input, like in the Terminal app.

`static let fileSystem: AccessibilityTextContentType`

A type that represents text used by a file browser, like in the Finder app in
macOS.

`static let messaging: AccessibilityTextContentType`

A type that represents text used in a message, like in the Messages app.

`static let narrative: AccessibilityTextContentType`

A type that represents text used in a story or poem, like in the Books app.

`static let plain: AccessibilityTextContentType`

A type that represents generic text that has no specific type.

`static let sourceCode: AccessibilityTextContentType`

A type that represents text used in source code, like in Swift Playgrounds.

`static let spreadsheet: AccessibilityTextContentType`

A type that represents text used in a grid of data, like in the Numbers app.

`static let wordProcessing: AccessibilityTextContentType`

A type that represents text used in a document, like in the Pages app.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Describing content

`func accessibilityTextContentType(AccessibilityTextContentType) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Sets an accessibility text content type.

`func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Sets the accessibility level of this heading.

`enum AccessibilityHeadingLevel`

The hierarchy of a heading in relation other headings.

Protocol

# AXChartDescriptorRepresentable

A type to generate an `AXChartDescriptor` object that you use to provide
information about a chart and its data for an accessible experience in
VoiceOver or other assistive technologies.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    protocol AXChartDescriptorRepresentable

## Overview

Note that you may use the `@Environment` property wrapper inside the
implementation of your `AXChartDescriptorRepresentable`, in which case you
should implement `updateChartDescriptor`, which will be called when the
`Environment` changes.

For example, to provide accessibility for a view that represents a chart, you
would first declare your chart descriptor representable type:

Then, provide an instance of your `AXChartDescriptorRepresentable` type to
your view using the `accessibilityChartDescriptor` modifier:

## Topics

### Managing a descriptor

`func makeChartDescriptor() -> AXChartDescriptor`

Create the `AXChartDescriptor` for this view, and return it.

**Required**

` func updateChartDescriptor(AXChartDescriptor)`

Update the existing `AXChartDescriptor` for your view, based on changes in
your view or in the `Environment`.

**Required** Default implementation provided.

## See Also

### Describing charts

`func accessibilityChartDescriptor<R>(R) -> some View`

Adds a descriptor to a View that represents a chart to make the chart’s
contents accessible to all users.

Structure

# AccessibilityCustomContentKey

Key used to specify the identifier and label associated with an entry of
additional accessibility information.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityCustomContentKey

## Overview

Use `AccessibilityCustomContentKey` and the associated modifiers taking this
value as a parameter in order to simplify clearing or replacing entries of
additional information that are manipulated from multiple places in your code.

## Topics

### Creating a key

`init(LocalizedStringKey)`

Create an `AccessibilityCustomContentKey` with the specified label.

`init(Text, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

`init(LocalizedStringKey, id: String)`

Create an `AccessibilityCustomContentKey` with the specified label and
identifier.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Adding custom descriptions

`func accessibilityCustomContent(AccessibilityCustomContentKey,
LocalizedStringKey, importance: AXCustomContent.Importance) ->
ModifiedContent<Self, AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(AccessibilityCustomContentKey, Text?,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(LocalizedStringKey, V, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(Text, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, LocalizedStringKey,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent<V>(AccessibilityCustomContentKey, V,
importance: AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

`func accessibilityCustomContent(LocalizedStringKey, Text, importance:
AXCustomContent.Importance) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Add additional accessibility information to the view.

Structure

# AccessibilityTraits

A set of accessibility traits that describe how an element behaves.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct AccessibilityTraits

## Topics

### Getting traits

`static let allowsDirectInteraction: AccessibilityTraits`

The accessibility element allows direct touch interaction for VoiceOver users.

`static let causesPageTurn: AccessibilityTraits`

The accessibility element causes an automatic page turn when VoiceOver
finishes reading the text within it.

`static let isButton: AccessibilityTraits`

The accessibility element is a button.

`static let isHeader: AccessibilityTraits`

The accessibility element is a header that divides content into sections, like
the title of a navigation bar.

`static let isImage: AccessibilityTraits`

The accessibility element is an image.

`static let isKeyboardKey: AccessibilityTraits`

The accessibility element behaves as a keyboard key.

`static let isLink: AccessibilityTraits`

The accessibility element is a link.

`static let isModal: AccessibilityTraits`

The accessibility element is modal.

`static let isSearchField: AccessibilityTraits`

The accessibility element is a search field.

`static let isSelected: AccessibilityTraits`

The accessibility element is currently selected.

`static let isStaticText: AccessibilityTraits`

The accessibility element is a static text that cannot be modified by the
user.

`static let isSummaryElement: AccessibilityTraits`

The accessibility element provides summary information when the application
starts.

`static let isToggle: AccessibilityTraits`

The accessibility element is a toggle.

`static let playsSound: AccessibilityTraits`

The accessibility element plays its own sound when activated.

`static let startsMediaSession: AccessibilityTraits`

The accessibility element starts a media session when it is activated.

`static let updatesFrequently: AccessibilityTraits`

The accessibility element frequently updates its label or value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Assigning traits to content

`func accessibilityAddTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Adds the given traits to the view.

`func accessibilityRemoveTraits(AccessibilityTraits) -> ModifiedContent<Self,
AccessibilityAttachmentModifier>`

Removes the given traits from this view.

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

