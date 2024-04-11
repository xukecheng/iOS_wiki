Initializer

# init(entity:insertInto:)

Initializes a managed object from an entity description and inserts it into
the specified managed object context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        entity: NSEntityDescription,
        insertInto context: NSManagedObjectContext?
    )

##  Parameters

`entity`

    

The entity of which to create an instance.

The model associated with `context`'s persistent store coordinator must
contain `entity`.

`context`

    

The context into which the new instance is inserted.

## Return Value

An initialized instance of the appropriate class for `entity`.

## Discussion

`NSManagedObject` uses dynamic class generation to support the Objective-C 2
properties feature (see Declared Properties) by automatically creating a
subclass of the class appropriate for `entity`.
`initWithEntity:insertIntoManagedObjectContext:` therefore returns an instance
of the appropriate class for `entity`. The dynamically-generated subclass will
be based on the class specified by the entity, so specifying a custom class in
your model will supersede the class passed to `alloc`.

If `context` is not `nil`, this method invokes `[context insertObject:self]`
(which causes `awakeFromInsert()` to be invoked).

You are discouraged from overriding this method—you should instead override
`awakeFromInsert()` and/or `awakeFromFetch()` (if there is logic common to
these methods, it should be factored into a third method which is invoked from
both). If you do perform custom initialization in this method, you may cause
problems with undo and redo operations.

In many applications, there is no need to subsequently assign a newly-created
managed object to a particular store—see `assign(_:to:)`. If your application
has multiple stores and you do need to assign an object to a specific store,
you should not do so in a managed object's initializer method. Such an
assignment is controller- not model-level logic.

Important

This method is the designated initializer for `NSManagedObject`. You must not
initialize a managed object simply by sending it `init`.

### Special Considerations

If you override `init(entity:insertInto:)`, you _must_ ensure that you set
`self` to the return value from invocation of `super`’s implementation, as
shown in the following example:

## See Also

### Creating a Managed Object

`init(context: NSManagedObjectContext)`

Initializes a managed object subclass and inserts it into the specified
managed object context.

### Related Documentation

Core Data Programming Guide

`class func insertNewObject(forEntityName: String, into:
NSManagedObjectContext) -> NSManagedObject`

Creates, configures, and returns an instance of the class for the entity with
a given name.

Initializer

# init(context:)

Initializes a managed object subclass and inserts it into the specified
managed object context.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    convenience init(context moc: NSManagedObjectContext)

## Return Value

An initialized instance of the appropriate subclass.

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that
represent a single entity in the model.

## See Also

### Creating a Managed Object

`init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)`

Initializes a managed object from an entity description and inserts it into
the specified managed object context.

Instance Property

# entity

The entity description of the managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entity: NSEntityDescription { get }

## Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting a Managed Object’s Identity

`var objectID: NSManagedObjectID`

The object ID of the managed object.

`class func entity() -> NSEntityDescription`

Returns the entity description that is associated with this subclass.

Instance Property

# objectID

The object ID of the managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var objectID: NSManagedObjectID { get }

## Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

Important

If the receiver has not yet been saved, the object ID is a temporary value
that will change when the object is saved.

## See Also

### Getting a Managed Object’s Identity

`var entity: NSEntityDescription`

The entity description of the managed object.

`class func entity() -> NSEntityDescription`

Returns the entity description that is associated with this subclass.

### Related Documentation

`func uriRepresentation() -> URL`

Returns a URI that provides an archiveable reference to the object for the
object ID.

Type Method

# entity()

Returns the entity description that is associated with this subclass.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class func entity() -> NSEntityDescription

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that
represent a single entity in the model.

## See Also

### Getting a Managed Object’s Identity

`var entity: NSEntityDescription`

The entity description of the managed object.

`var objectID: NSManagedObjectID`

The object ID of the managed object.

Instance Property

# managedObjectContext

The managed object context with which the managed object is registered.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get }

## Discussion

May be `nil` if the receiver has been deleted from its context.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# hasChanges

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var hasChanges: Bool { get }

## Discussion

`true` if the receiver has been inserted, has been deleted, or has unsaved
changes, otherwise `false`. The result is the equivalent of OR-ing the values
of `isInserted`, `isDeleted`, and `isUpdated`.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# isInserted

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isInserted: Bool { get }

## Discussion

`true` if the receiver has been inserted in a managed object context,
otherwise `false`. If the receiver is a fault, accessing this property does
not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# isUpdated

A Boolean value that indicates whether the managed object has unsaved changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isUpdated: Bool { get }

## Discussion

`true` if the receiver has unsaved changes, otherwise `false`. The receiver
has unsaved changes if it has been updated since its managed object context
was last saved.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# isDeleted

A Boolean value that indicates whether the managed object will be deleted
during the next save.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isDeleted: Bool { get }

## Discussion

`true` if Core Data will ask the persistent store to delete the object during
the next save operation, otherwise `false`. It may return `false` at other
times, particularly after the object has been deleted. The immediacy with
which it will stop returning `true` depends on where the object is in the
process of being deleted.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

### Related Documentation

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

Instance Property

# isFault

A Boolean value that indicates whether the managed object is a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isFault: Bool { get }

## Discussion

`true` if the receiver is a fault, otherwise `false`. Knowing whether an
object is a fault is useful in many situations when computations are optional.
It can also be used to avoid growing the object graph unnecessarily (which may
improve performance as it can avoid time-consuming fetches from data stores).

If this property is `false`, then the receiver's data must be in memory.
However, if this property is `true`, it does _not_ mean that the data is not
in memory. The data may be in memory, or it may not, depending on many factors
influencing caching.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# faultingState

The faulting state of the managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var faultingState: Int { get }

## Return Value

`0` if the object is fully initialized as a managed object and not
transitioning to or from another state, otherwise some other value.

## Discussion

`0` if the object is fully initialized as a managed object and not
transitioning to or from another state, otherwise some other value. This
property allows you to determine if an object is in a transitional phase when
receiving a key-value observing change notification.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Method

# hasFault(forRelationshipNamed:)

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func hasFault(forRelationshipNamed key: String) -> Bool

##  Parameters

`key`

    

The name of one of the receiver’s relationships.

## Return Value

`true` if the relationship for `key` is a fault; otherwise, `false`.

## Discussion

If the specified relationship is a fault, calling this method does not result
in the fault firing.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# hasPersistentChangedValues

A Boolean value that indicates whether the managed object has persistent
changes.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var hasPersistentChangedValues: Bool { get }

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

Type Property

# contextShouldIgnoreUnmodeledPropertyChanges

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class var contextShouldIgnoreUnmodeledPropertyChanges: Bool { get }

## Return Value

`false` if instances of the class should be marked as having changes if an
unmodeled property is changed, otherwise `true`.

## Discussion

The default value is `true`.

## See Also

### Managing Change Events

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

### Related Documentation

`var hasChanges: Bool`

A Boolean value that indicates whether the context has uncommitted changes.

Instance Method

# awakeFromFetch()

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func awakeFromFetch()

## Discussion

You typically use this method to compute derived values or to recreate
transient relationships from the receiver’s persistent properties.

The managed object context’s change processing is explicitly disabled around
this method so that you can use public setters to establish transient values
and other caches without dirtying the object or its context. Because of this,
however, you should not modify relationships in this method as the inverse
will not be set.

Important

Subclasses must invoke super’s implementation before performing their own
initialization.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

### Related Documentation

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

Instance Method

# awakeFromInsert()

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func awakeFromInsert()

## Discussion

You typically use this method to initialize special default property values.
This method is invoked only once in the object's lifetime.

If you want to set attribute values in an implementation of this method, you
should typically use primitive accessor methods (either
`setPrimitiveValue(_:forKey:)` or—better—the appropriate custom primitive
accessors). This ensures that the new values are treated as baseline values
rather than being recorded as undoable changes for the properties in question.

Important

Subclasses must invoke super’s implementation before performing their own
initialization.

### Special Considerations

If you create a managed object then perform undo operations to bring the
managed object context to a state prior to the object’s creation, then perform
redo operations to bring the managed object context back to a state after the
object’s creation, `awakeFromInsert()` is _not_ invoked a second time.

You are typically discouraged from performing fetches within an implementation
of `awakeFromInsert()`. Although it is allowed, execution of the fetch request
can trigger the sending of internal Core Data notifications which may have
unwanted side-effects. For example, in macOS, an instance of
`NSArrayController` may end up inserting a new object into its content array
twice.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# awake(fromSnapshotEvents:)

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func awake(fromSnapshotEvents flags: NSSnapshotEventType)

##  Parameters

`flags`

    

A bit mask of `didChangeValue(forKey:)` constants to denote the event or
events that led to the method being invoked.

For possible values, see `NSSnapshotEventType`.

## Discussion

You typically use this method to compute derived values or to recreate
transient relationships from the receiver’s persistent properties.

If you want to set attribute values and need to avoid emitting key-value
observation change notifications, you should use primitive accessor methods
(either `setPrimitiveValue(_:forKey:)` or—better—the appropriate custom
primitive accessors). This ensures that the new values are treated as baseline
values rather than being recorded as undoable changes for the properties in
question.

Important

Subclasses must invoke super’s implementation before performing their own
initialization.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# changedValues()

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func changedValues() -> [String : Any]

## Return Value

A dictionary with keys that are the names of persistent properties with
changes since last fetching or saving the receiver, and with the new values
for those properties.

## Discussion

This method only reports changes to properties that are persistent properties
of the receiver, not changes to transient properties or custom instance
variables.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# changedValuesForCurrentEvent()

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func changedValuesForCurrentEvent() -> [String : Any]

## Return Value

A dictionary with keys that are the names of persistent properties with
changes since the last posting of `NSManagedObjectContextObjectsDidChange`,
and with the new values for those properties.

## Discussion

This method only reports changes to properties that are persistent properties
of the receiver, not changes to transient properties or custom instance
variables.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# committedValues(forKeys:)

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func committedValues(forKeys keys: [String]?) -> [String : Any]

##  Parameters

`keys`

    

An array containing names of properties of the receiver, or `nil`.

## Return Value

A dictionary containing the last fetched or saved values of the receiver for
the properties specified by `keys`.

## Discussion

`nil` values are represented by an instance of `NSNull`.

This method only reports values of properties that are defined as persistent
properties of the receiver, not values of transient properties or of custom
instance variables.

You can invoke this method with the `keys` value of `nil` to retrieve
committed values for all the receiver’s properties, as illustrated by the
following example.

It is more efficient to use `nil` than to pass an array of all the property
keys.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# prepareForDeletion()

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func prepareForDeletion()

## Discussion

You can implement this method to perform any operations required before the
object is deleted, such as custom propagation before relationships are torn
down, or reconfiguration of objects using key-value observing.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# willSave()

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willSave()

## Discussion

This method can have “side effects” on persistent values. You can use it to,
for example, compute persistent values from other transient or scratchpad
values.

If you want to update a persistent property value, you should typically test
for equality of any new value with the existing value before making a change.
If you change property values using standard accessor methods, Core Data will
observe the resultant change notification and so invoke `willSave` again
before saving the object’s managed object context. If you continue to modify a
value in `willSave`, `willSave` will continue to be called until your program
crashes.

For example, if you set a last-modified timestamp, you should check whether
either you previously set it in the same save operation, or that the existing
timestamp is not less than a small delta from the current time. Typically it’s
better to calculate the timestamp once for all the objects being saved (for
example, in response to an `NSManagedObjectContextWillSaveNotification`).

If you change property values using primitive accessors, you avoid the
possibility of infinite recursion, but Core Data will not notice the change
you make.

The sense of “save” in the method name is that of a database commit statement
and so applies to deletions as well as to updates to objects. For subclasses,
this method is therefore an appropriate locus for code to be executed when an
object deleted as well as “saved to disk.” You can find out if an object is
marked for deletion with `isDeleted`.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# didSave()

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didSave()

## Discussion

You can use this method to notify other objects after a save, and to compute
transient values from persistent values.

This method can have “side effects” on the persistent values, however any
changes you make using standard accessor methods will by default dirty the
managed object context and leave your context with unsaved changes. Moreover,
if the object’s context has an undo manager, such changes will add an undo
operation. For document-based applications, changes made in `didSave` will
therefore come into the next undo grouping, which can lead to “empty” undo
operations from the user's perspective. You may want to disable undo
registration to avoid this issue.

The sense of “save” in the method name is that of a database commit statement
and so applies to deletions as well as to updates to objects. For subclasses,
this method is therefore an appropriate locus for code to be executed when an
object deleted as well as “saved to disk.” You can find out if an object is
marked for deletion with `isDeleted`.

### Special Considerations

You cannot attempt to resurrect a deleted object in `didSave`.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# willTurnIntoFault()

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willTurnIntoFault()

## Discussion

This method is the companion of the `didTurnIntoFault()` method. You can use
it to (re)set state which requires access to property values (for example,
observers across key paths). The default implementation does nothing.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# didTurnIntoFault()

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didTurnIntoFault()

## Discussion

You use this method to clear out custom data caches—transient values declared
as entity properties are typically already cleared out by the time this method
is invoked (see, for example, `refresh(_:mergeChanges:)`).

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Type Method

# fetchRequest()

Returns an initialized fetch request with the entity this subclass represents.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.0+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+  Xcode 8.0+

    
    
    @objc
    dynamic class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that
represent a single entity in the model.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Property

# objectWillChange

A publisher that emits before the object changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+  Xcode 11.0+

    
    
    var objectWillChange: ObservableObjectPublisher { get }

## Relationships

### From Protocol

  * `ObservableObject`

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Type Alias

# NSManagedObject.ObjectWillChangePublisher

An object that publishes changes from observable objects.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 11.0+

    
    
    typealias ObjectWillChangePublisher = ObservableObjectPublisher

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

Instance Method

# value(forKey:)

Returns the value for the property specified by `key`.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func value(forKey key: String) -> Any?

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Return Value

The value of the property specified by `key`.

## Discussion

If `key` is not a property defined by the model, the method raises an
exception. This method is overridden by `NSManagedObject` to access the
managed object’s generic dictionary storage unless the receiver’s class
explicitly provides key-value coding compliant accessor methods for `key`.

Important

You must not override this method.

## See Also

### Supporting Key-Value Coding

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

Instance Method

# setValue(_:forKey:)

Sets the specified property of the managed object to the specified value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setValue(
        _ value: Any?,
        forKey key: String
    )

##  Parameters

`value`

    

The new value for the property specified by `key`.

`key`

    

The name of one of the receiver's properties.

## Discussion

If `key` is not a property defined by the model, the method raises an
exception. If `key` identifies a to-one relationship, relates the object
specified by `value` to the receiver, unrelating the previously related object
if there was one. Given a collection object and a key that identifies a to-
many relationship, relates the objects contained in the collection to the
receiver, unrelating previously related objects if there were any.

This method is overridden by `NSManagedObject` to access the managed object’s
generic dictionary storage unless the receiver’s class explicitly provides
key-value coding compliant accessor methods for `key`.

Important

You must not override this method.

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

Instance Method

# primitiveValue(forKey:)

Returns the value for the specified property from the managed object’s private
internal storage .

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func primitiveValue(forKey key: String) -> Any?

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Return Value

The value of the property specified by `key`. Returns `nil` if no value has
been set.

## Discussion

This method does not invoke the access notification methods
(`willAccessValue(forKey:)` and `didAccessValue(forKey:)`). This method is
used primarily by subclasses that implement custom accessor methods that need
direct access to the receiver’s private storage.

### Special Considerations

Subclasses should not override this method.

The following points also apply:

  * Primitive accessor methods are only supported on _modeled_ properties. If you invoke a primitive accessor on an unmodeled property, it will instead operate upon a random modeled property. (The debug libraries and frameworks (available from Apple Developer Website) have assertions to test for passing unmodeled keys to these methods.)

  * You are strongly encouraged to use the dynamically-generated accessors rather than using this method directly (for example, `primitiveName:` instead of `primitiveValueForKey:@"name"`). The dynamic accessors are much more efficient, and allow for compile-time checking.

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`mutableSetValueForKey:`

Returns a mutable set that provides read-write access to the unordered to-many
relationship specified by a given key.

Instance Method

# setPrimitiveValue(_:forKey:)

Sets the value of a given property in the managed object's private internal
storage.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setPrimitiveValue(
        _ value: Any?,
        forKey key: String
    )

##  Parameters

`value`

    

The new value for the property specified by `key`.

`key`

    

The name of one of the receiver's properties.

## Discussion

Sets in the receiver’s private internal storage the value of the property
specified by `key` to `value`. If `key` identifies a to-one relationship,
relates the object specified by `value` to the receiver, unrelating the
previously related object if there was one. Given a collection object and a
key that identifies a to-many relationship, relates the objects contained in
the collection to the receiver, unrelating previously related objects if there
were any.

This method does not invoke the change notification methods
(`willChangeValue(forKey:)` and `didChangeValue(forKey:)`). It is typically
used by subclasses that implement custom accessor methods that need direct
access to the receiver’s private internal storage. It is also used by the Core
Data framework to initialize the receiver with values from a persistent store
or to restore a value from a snapshot.

### Special Considerations

You must not override this method.

You should typically use this method only to modify attributes (usually
transient), not relationships. If you try to set a to-many relationship to a
new `NSMutableSet` object, it will (eventually) fail. In the unusual event
that you need to modify a relationship using this method, you first get the
existing set using `primitiveValueForKey:` (ensure the method does not return
`nil`), create a mutable copy, and then modify the copy—as illustrated in the
following example:

If the relationship is bi-directional (that is, if an inverse relationship is
specified) then you are also responsible for maintaining the inverse
relationship (regardless of cardinality)—in contrast with Core Data's normal
behavior described in Using Managed Objects.

The following points also apply:

  * Primitive accessor methods are only supported on _modeled_ properties. If you invoke a primitive accessor on an unmodeled property, it will instead operate upon a random modeled property. (The debug libraries and frameworks from (available from the Apple Developer Website) have assertions to test for passing unmodeled keys to these methods.)

  * You are strongly encouraged to use the dynamically-generated accessors rather than using this method directly (for example, `setPrimitiveName:` instead of `setPrimitiveValue:newName forKey:@"name"`). The dynamic accessors are much more efficient, and allow for compile-time checking.

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`mutableSetValueForKey:`

Returns a mutable set that provides read-write access to the unordered to-many
relationship specified by a given key.

Instance Method

# objectIDs(forRelationshipNamed:)

Returns the object IDs for all of the managed objects that are in the named
relationship.

iOS 8.3+  iPadOS 8.3+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func objectIDs(forRelationshipNamed key: String) -> [NSManagedObjectID]

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

Instance Method

# validateValue(_:forKey:)

Validates a property value for a given key.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateValue(
        _ value: AutoreleasingUnsafeMutablePointer<AnyObject?>,
        forKey key: String
    ) throws

##  Parameters

`value`

    

A pointer to an object.

`key`

    

The name of one of the receiver's properties.

`error`

    

If `value` is not a valid value for `key` (and cannot be coerced), upon return
contains an instance of `NSError` that describes the problem.

## Return Value

`true` if `value` is a valid value for `key` (or if `value` can be coerced
into a valid value for `key`), otherwise `false`.

## Discussion

This method is responsible for two things: coercing the value into an
appropriate type for the object, and validating it according to the object’s
rules.

The default implementation provided by `NSManagedObject` consults the object’s
entity description to coerce the value and to check for basic errors, such as
a null value when that isn’t allowed and the length of strings when a field
width is specified for the attribute. It then searches for a method of the
form `validate<Key>:error:` and invokes it if it exists.

You can implement methods of the form `validate<Key>:error:` to perform
validation that is not possible using the constraints available in the
property description. If it finds an unacceptable value, your validation
method should return `false` and in `error` an `NSError` object that describes
the problem. For more details, see Managed Object Validation. For inter-
property validation (to check for combinations of values that are invalid),
see `validateForUpdate()` and related methods.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Instance Method

# validateForDelete()

Determines whether the managed object can be deleted in its current state.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateForDelete() throws

##  Parameters

`error`

    

If the receiver cannot be deleted in its current state, upon return contains
an instance of `NSError` that describes the problem.

## Return Value

`true` if the receiver can be deleted in its current state, otherwise `false`.

## Discussion

An object cannot be deleted if it has a relationship has a “deny” delete rule
and that relationship has a destination object.

`NSManagedObject`’s implementation sends the receiver’s entity description a
message which performs basic checking based on the presence or absence of
values.

Important

Subclasses should invoke super’s implementation before performing their own
validation, and should combine any error returned by super’s implementation
with their own (see Managed Object Validation).

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Instance Method

# validateForInsert()

Determines whether the managed object can be inserted in its current state.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateForInsert() throws

##  Parameters

`error`

    

If the receiver cannot be inserted in its current state, upon return contains
an instance of `NSError` that describes the problem.

## Return Value

`true` if the receiver can be inserted in its current state, otherwise
`false`.

## Discussion

Subclasses should invoke super’s implementation before performing their own
validation, and should combine any error returned by super’s implementation
with their own (see Managed Object Validation).

### Discussion

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Instance Method

# validateForUpdate()

Determines whether the managed object's current state is valid.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateForUpdate() throws

##  Parameters

`error`

    

If the receiver's current state is invalid, upon return contains an instance
of `NSError` that describes the problem.

## Return Value

`true` if the receiver's current state is valid, otherwise `false`.

## Discussion

`NSManagedObject`’s implementation iterates through all of the receiver’s
properties validating each in turn. If this results in more than one error,
the `userInfo` dictionary in the `NSError` returned in `error` contains a key
`NSDetailedErrorsKey`; the corresponding value is an array containing the
individual validation errors. If you pass `NULL` as the error, validation will
abort after the first failure.

Important

Subclasses should invoke super’s implementation before performing their own
validation, and should combine any error returned by super’s implementation
with their own (see Managed Object Validation).

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationKeyErrorKey

The error key for the attribute that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationKeyErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationObjectErrorKey

The error key for the object that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationObjectErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationPredicateErrorKey

The error key for the predicate that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationPredicateErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationValueErrorKey

The error key for the value that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationValueErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

Instance Method

# didAccessValue(forKey:)

Provides support for key-value observing access notification.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didAccessValue(forKey key: String?)

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Discussion

Together with `willAccessValue(forKey:)`, this method is used to fire faults,
to maintain inverse relationships, and so on. Each read access must be wrapped
in this method pair (in the same way that each write access must be wrapped in
the `willChangeValueForKey:`/`didChangeValueForKey:` method pair). In the
default implementation of `NSManagedObject` these methods are invoked for you
automatically. If, say, you create a custom subclass that uses explicit
instance variables, you must invoke them yourself, as in the following
example.

## See Also

### Supporting Key-Value Observing

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# observationInfo()

Returns the observation info of the managed object.

macOS 10.4+  Mac Catalyst 13.1+

    
    
    func observationInfo() -> UnsafeMutableRawPointer?

## Return Value

The observation info of the receiver.

## Discussion

For more about key-value observation, see Key-Value Observing Programming
Guide.

Important

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# setObservationInfo(_:)

Sets the observation info of the managed object.

macOS 10.4+  Mac Catalyst 13.1+

    
    
    func setObservationInfo(_ inObservationInfo: UnsafeMutableRawPointer?)

##  Parameters

`value`

    

The new observation info for the receiver.

## Discussion

For more about observation information, see Key-Value Observing Programming
Guide.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# willAccessValue(forKey:)

Provides support for key-value observing access notification.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willAccessValue(forKey key: String?)

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Discussion

See `didAccessValue(forKey:)` for more details. You can invoke this method
with the `key` value of `nil` to ensure that a fault has been fired, as
illustrated by the following example.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# didChangeValue(forKey:)

Provides an opportunity to respond when a value of a given property has
changed.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didChangeValue(forKey key: String)

##  Parameters

`key`

    

The name of the property that changed.

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# didChangeValue(forKey:withSetMutation:using:)

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didChangeValue(
        forKey inKey: String,
        withSetMutation inMutationKind: NSKeyValueSetMutationKind,
        using inObjects: Set<AnyHashable>
    )

##  Parameters

`inKey`

    

The name of a property that is a to-many relationship.

`inMutationKind`

    

The type of change that was made.

`inObjects`

    

The objects that were involved in the change (see
`NSKeyValueSetMutationKind`).

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# willChangeValue(forKey:)

Provides an opportunity to respond when a value of a given property is about
to change.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willChangeValue(forKey key: String)

##  Parameters

`key`

    

The name of the property that will change.

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# willChangeValue(forKey:withSetMutation:using:)

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willChangeValue(
        forKey inKey: String,
        withSetMutation inMutationKind: NSKeyValueSetMutationKind,
        using inObjects: Set<AnyHashable>
    )

##  Parameters

`inKey`

    

The name of a property that is a to-many relationship

`inMutationKind`

    

The type of change that will be made.

`inObjects`

    

The objects that were involved in the change (see
`NSKeyValueSetMutationKind`).

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

Initializer

# init(entity:insertInto:)

Initializes a managed object from an entity description and inserts it into
the specified managed object context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    init(
        entity: NSEntityDescription,
        insertInto context: NSManagedObjectContext?
    )

##  Parameters

`entity`

    

The entity of which to create an instance.

The model associated with `context`'s persistent store coordinator must
contain `entity`.

`context`

    

The context into which the new instance is inserted.

## Return Value

An initialized instance of the appropriate class for `entity`.

## Discussion

`NSManagedObject` uses dynamic class generation to support the Objective-C 2
properties feature (see Declared Properties) by automatically creating a
subclass of the class appropriate for `entity`.
`initWithEntity:insertIntoManagedObjectContext:` therefore returns an instance
of the appropriate class for `entity`. The dynamically-generated subclass will
be based on the class specified by the entity, so specifying a custom class in
your model will supersede the class passed to `alloc`.

If `context` is not `nil`, this method invokes `[context insertObject:self]`
(which causes `awakeFromInsert()` to be invoked).

You are discouraged from overriding this method—you should instead override
`awakeFromInsert()` and/or `awakeFromFetch()` (if there is logic common to
these methods, it should be factored into a third method which is invoked from
both). If you do perform custom initialization in this method, you may cause
problems with undo and redo operations.

In many applications, there is no need to subsequently assign a newly-created
managed object to a particular store—see `assign(_:to:)`. If your application
has multiple stores and you do need to assign an object to a specific store,
you should not do so in a managed object's initializer method. Such an
assignment is controller- not model-level logic.

Important

This method is the designated initializer for `NSManagedObject`. You must not
initialize a managed object simply by sending it `init`.

### Special Considerations

If you override `init(entity:insertInto:)`, you _must_ ensure that you set
`self` to the return value from invocation of `super`’s implementation, as
shown in the following example:

    
    
    - (id)initWithEntity:(NSEntityDescription*)entity insertIntoManagedObjectContext:(NSManagedObjectContext*)context
    {
        self = [super initWithEntity:entity insertIntoManagedObjectContext:context];
        if (self != nil) {
            // Perform additional initialization.
        }
        return self;
    }
    

## See Also

### Creating a Managed Object

`init(context: NSManagedObjectContext)`

Initializes a managed object subclass and inserts it into the specified
managed object context.

### Related Documentation

Core Data Programming Guide

`class func insertNewObject(forEntityName: String, into:
NSManagedObjectContext) -> NSManagedObject`

Creates, configures, and returns an instance of the class for the entity with
a given name.

Initializer

# init(context:)

Initializes a managed object subclass and inserts it into the specified
managed object context.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    convenience init(context moc: NSManagedObjectContext)

## Return Value

An initialized instance of the appropriate subclass.

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that
represent a single entity in the model.

## See Also

### Creating a Managed Object

`init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)`

Initializes a managed object from an entity description and inserts it into
the specified managed object context.

Instance Property

# entity

The entity description of the managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var entity: NSEntityDescription { get }

## Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting a Managed Object’s Identity

`var objectID: NSManagedObjectID`

The object ID of the managed object.

`class func entity() -> NSEntityDescription`

Returns the entity description that is associated with this subclass.

Instance Property

# objectID

The object ID of the managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var objectID: NSManagedObjectID { get }

## Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

Important

If the receiver has not yet been saved, the object ID is a temporary value
that will change when the object is saved.

## See Also

### Getting a Managed Object’s Identity

`var entity: NSEntityDescription`

The entity description of the managed object.

`class func entity() -> NSEntityDescription`

Returns the entity description that is associated with this subclass.

### Related Documentation

`func uriRepresentation() -> URL`

Returns a URI that provides an archiveable reference to the object for the
object ID.

Type Method

# entity()

Returns the entity description that is associated with this subclass.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.1+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+

    
    
    class func entity() -> NSEntityDescription

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that
represent a single entity in the model.

## See Also

### Getting a Managed Object’s Identity

`var entity: NSEntityDescription`

The entity description of the managed object.

`var objectID: NSManagedObjectID`

The object ID of the managed object.

Instance Property

# managedObjectContext

The managed object context with which the managed object is registered.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    unowned(unsafe) var managedObjectContext: NSManagedObjectContext? { get }

## Discussion

May be `nil` if the receiver has been deleted from its context.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# hasChanges

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var hasChanges: Bool { get }

## Discussion

`true` if the receiver has been inserted, has been deleted, or has unsaved
changes, otherwise `false`. The result is the equivalent of OR-ing the values
of `isInserted`, `isDeleted`, and `isUpdated`.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# isInserted

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isInserted: Bool { get }

## Discussion

`true` if the receiver has been inserted in a managed object context,
otherwise `false`. If the receiver is a fault, accessing this property does
not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# isUpdated

A Boolean value that indicates whether the managed object has unsaved changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isUpdated: Bool { get }

## Discussion

`true` if the receiver has unsaved changes, otherwise `false`. The receiver
has unsaved changes if it has been updated since its managed object context
was last saved.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# isDeleted

A Boolean value that indicates whether the managed object will be deleted
during the next save.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isDeleted: Bool { get }

## Discussion

`true` if Core Data will ask the persistent store to delete the object during
the next save operation, otherwise `false`. It may return `false` at other
times, particularly after the object has been deleted. The immediacy with
which it will stop returning `true` depends on where the object is in the
process of being deleted.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

### Related Documentation

`var deletedObjects: Set<NSManagedObject>`

The set of objects that will be removed from their persistent store during the
next save operation.

`static let NSManagedObjectContextObjectsDidChange: NSNotification.Name`

A notification of changes made to managed objects associated with this
context.

Instance Property

# isFault

A Boolean value that indicates whether the managed object is a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var isFault: Bool { get }

## Discussion

`true` if the receiver is a fault, otherwise `false`. Knowing whether an
object is a fault is useful in many situations when computations are optional.
It can also be used to avoid growing the object graph unnecessarily (which may
improve performance as it can avoid time-consuming fetches from data stores).

If this property is `false`, then the receiver's data must be in memory.
However, if this property is `true`, it does _not_ mean that the data is not
in memory. The data may be in memory, or it may not, depending on many factors
influencing caching.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# faultingState

The faulting state of the managed object.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var faultingState: Int { get }

## Return Value

`0` if the object is fully initialized as a managed object and not
transitioning to or from another state, otherwise some other value.

## Discussion

`0` if the object is fully initialized as a managed object and not
transitioning to or from another state, otherwise some other value. This
property allows you to determine if an object is in a transitional phase when
receiving a key-value observing change notification.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Method

# hasFault(forRelationshipNamed:)

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func hasFault(forRelationshipNamed key: String) -> Bool

##  Parameters

`key`

    

The name of one of the receiver’s relationships.

## Return Value

`true` if the relationship for `key` is a fault; otherwise, `false`.

## Discussion

If the specified relationship is a fault, calling this method does not result
in the fault firing.

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`var hasPersistentChangedValues: Bool`

A Boolean value that indicates whether the managed object has persistent
changes.

Instance Property

# hasPersistentChangedValues

A Boolean value that indicates whether the managed object has persistent
changes.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var hasPersistentChangedValues: Bool { get }

## See Also

### Getting State Information

`var managedObjectContext: NSManagedObjectContext?`

The managed object context with which the managed object is registered.

`var hasChanges: Bool`

A Boolean value that indicates whether the managed object has been inserted,
has been deleted, or has unsaved changes.

`var isInserted: Bool`

A Boolean value that indicates whether the managed object has been inserted in
a managed object context.

`var isUpdated: Bool`

A Boolean value that indicates whether the managed object has unsaved changes.

`var isDeleted: Bool`

A Boolean value that indicates whether the managed object will be deleted
during the next save.

`var isFault: Bool`

A Boolean value that indicates whether the managed object is a fault.

`var faultingState: Int`

The faulting state of the managed object.

`func hasFault(forRelationshipNamed: String) -> Bool`

Returns a Boolean value that indicates whether the relationship for a given
key is a fault.

Type Property

# contextShouldIgnoreUnmodeledPropertyChanges

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    class var contextShouldIgnoreUnmodeledPropertyChanges: Bool { get }

## Return Value

`false` if instances of the class should be marked as having changes if an
unmodeled property is changed, otherwise `true`.

## Discussion

The default value is `true`.

## See Also

### Managing Change Events

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

### Related Documentation

`var hasChanges: Bool`

A Boolean value that indicates whether the context has uncommitted changes.

Instance Method

# awakeFromFetch()

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func awakeFromFetch()

## Discussion

You typically use this method to compute derived values or to recreate
transient relationships from the receiver’s persistent properties.

The managed object context’s change processing is explicitly disabled around
this method so that you can use public setters to establish transient values
and other caches without dirtying the object or its context. Because of this,
however, you should not modify relationships in this method as the inverse
will not be set.

Important

Subclasses must invoke super’s implementation before performing their own
initialization.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

### Related Documentation

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

Instance Method

# awakeFromInsert()

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func awakeFromInsert()

## Discussion

You typically use this method to initialize special default property values.
This method is invoked only once in the object's lifetime.

If you want to set attribute values in an implementation of this method, you
should typically use primitive accessor methods (either
`setPrimitiveValue(_:forKey:)` or—better—the appropriate custom primitive
accessors). This ensures that the new values are treated as baseline values
rather than being recorded as undoable changes for the properties in question.

Important

Subclasses must invoke super’s implementation before performing their own
initialization.

### Special Considerations

If you create a managed object then perform undo operations to bring the
managed object context to a state prior to the object’s creation, then perform
redo operations to bring the managed object context back to a state after the
object’s creation, `awakeFromInsert()` is _not_ invoked a second time.

You are typically discouraged from performing fetches within an implementation
of `awakeFromInsert()`. Although it is allowed, execution of the fetch request
can trigger the sending of internal Core Data notifications which may have
unwanted side-effects. For example, in macOS, an instance of
`NSArrayController` may end up inserting a new object into its content array
twice.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# awake(fromSnapshotEvents:)

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func awake(fromSnapshotEvents flags: NSSnapshotEventType)

##  Parameters

`flags`

    

A bit mask of `didChangeValue(forKey:)` constants to denote the event or
events that led to the method being invoked.

For possible values, see `NSSnapshotEventType`.

## Discussion

You typically use this method to compute derived values or to recreate
transient relationships from the receiver’s persistent properties.

If you want to set attribute values and need to avoid emitting key-value
observation change notifications, you should use primitive accessor methods
(either `setPrimitiveValue(_:forKey:)` or—better—the appropriate custom
primitive accessors). This ensures that the new values are treated as baseline
values rather than being recorded as undoable changes for the properties in
question.

Important

Subclasses must invoke super’s implementation before performing their own
initialization.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# changedValues()

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func changedValues() -> [String : Any]

## Return Value

A dictionary with keys that are the names of persistent properties with
changes since last fetching or saving the receiver, and with the new values
for those properties.

## Discussion

This method only reports changes to properties that are persistent properties
of the receiver, not changes to transient properties or custom instance
variables.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# changedValuesForCurrentEvent()

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func changedValuesForCurrentEvent() -> [String : Any]

## Return Value

A dictionary with keys that are the names of persistent properties with
changes since the last posting of `NSManagedObjectContextObjectsDidChange`,
and with the new values for those properties.

## Discussion

This method only reports changes to properties that are persistent properties
of the receiver, not changes to transient properties or custom instance
variables.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# committedValues(forKeys:)

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func committedValues(forKeys keys: [String]?) -> [String : Any]

##  Parameters

`keys`

    

An array containing names of properties of the receiver, or `nil`.

## Return Value

A dictionary containing the last fetched or saved values of the receiver for
the properties specified by `keys`.

## Discussion

`nil` values are represented by an instance of `NSNull`.

This method only reports values of properties that are defined as persistent
properties of the receiver, not values of transient properties or of custom
instance variables.

You can invoke this method with the `keys` value of `nil` to retrieve
committed values for all the receiver’s properties, as illustrated by the
following example.

    
    
    NSDictionary *allCommittedValues =
            [aManagedObject committedValuesForKeys:nil];
    

It is more efficient to use `nil` than to pass an array of all the property
keys.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# prepareForDeletion()

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func prepareForDeletion()

## Discussion

You can implement this method to perform any operations required before the
object is deleted, such as custom propagation before relationships are torn
down, or reconfiguration of objects using key-value observing.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# willSave()

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willSave()

## Discussion

This method can have “side effects” on persistent values. You can use it to,
for example, compute persistent values from other transient or scratchpad
values.

If you want to update a persistent property value, you should typically test
for equality of any new value with the existing value before making a change.
If you change property values using standard accessor methods, Core Data will
observe the resultant change notification and so invoke `willSave` again
before saving the object’s managed object context. If you continue to modify a
value in `willSave`, `willSave` will continue to be called until your program
crashes.

For example, if you set a last-modified timestamp, you should check whether
either you previously set it in the same save operation, or that the existing
timestamp is not less than a small delta from the current time. Typically it’s
better to calculate the timestamp once for all the objects being saved (for
example, in response to an `NSManagedObjectContextWillSaveNotification`).

If you change property values using primitive accessors, you avoid the
possibility of infinite recursion, but Core Data will not notice the change
you make.

The sense of “save” in the method name is that of a database commit statement
and so applies to deletions as well as to updates to objects. For subclasses,
this method is therefore an appropriate locus for code to be executed when an
object deleted as well as “saved to disk.” You can find out if an object is
marked for deletion with `isDeleted`.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# didSave()

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didSave()

## Discussion

You can use this method to notify other objects after a save, and to compute
transient values from persistent values.

This method can have “side effects” on the persistent values, however any
changes you make using standard accessor methods will by default dirty the
managed object context and leave your context with unsaved changes. Moreover,
if the object’s context has an undo manager, such changes will add an undo
operation. For document-based applications, changes made in `didSave` will
therefore come into the next undo grouping, which can lead to “empty” undo
operations from the user's perspective. You may want to disable undo
registration to avoid this issue.

The sense of “save” in the method name is that of a database commit statement
and so applies to deletions as well as to updates to objects. For subclasses,
this method is therefore an appropriate locus for code to be executed when an
object deleted as well as “saved to disk.” You can find out if an object is
marked for deletion with `isDeleted`.

### Special Considerations

You cannot attempt to resurrect a deleted object in `didSave`.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# willTurnIntoFault()

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willTurnIntoFault()

## Discussion

This method is the companion of the `didTurnIntoFault()` method. You can use
it to (re)set state which requires access to property values (for example,
observers across key paths). The default implementation does nothing.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Method

# didTurnIntoFault()

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didTurnIntoFault()

## Discussion

You use this method to clear out custom data caches—transient values declared
as entity properties are typically already cleared out by the time this method
is invoked (see, for example, `refresh(_:mergeChanges:)`).

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Type Method

# fetchRequest()

Returns an initialized fetch request with the entity this subclass represents.

iOS 10.0+  iPadOS 10.0+  macOS 10.12+  Mac Catalyst 13.0+  tvOS 10.0+  watchOS
3.0+  visionOS 1.0+  Xcode 8.0+

    
    
    @objc
    dynamic class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>

## Discussion

This method is only legal to call on subclasses of `NSManagedObject` that
represent a single entity in the model.

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Instance Property

# objectWillChange

A publisher that emits before the object changes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+  Xcode 11.0+

    
    
    var objectWillChange: ObservableObjectPublisher { get }

## Relationships

### From Protocol

  * `ObservableObject`

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`typealias NSManagedObject.ObjectWillChangePublisher`

An object that publishes changes from observable objects.

Type Alias

# NSManagedObject.ObjectWillChangePublisher

An object that publishes changes from observable objects.

iOS 7.0+  iPadOS 7.0+  macOS 10.9+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+  Xcode 11.0+

    
    
    typealias ObjectWillChangePublisher = ObservableObjectPublisher

## See Also

### Managing Change Events

`class var contextShouldIgnoreUnmodeledPropertyChanges: Bool`

A Boolean value that indicates whether to mark instances of the class as
having changes when an unmodeled property changes.

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`func awakeFromInsert()`

Provides an opportunity to add code into the life cycle of the managed object
when initially creating it.

`func awake(fromSnapshotEvents: NSSnapshotEventType)`

Provides an opportunity to add code into the life cycle of the managed object
when fulfilling it from a snapshot.

`func changedValues() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func changedValuesForCurrentEvent() -> [String : Any]`

Returns a dictionary containing the keys and new values of persistent
properties with changes since the last fetching or saving of the managed
object.

`func committedValues(forKeys: [String]?) -> [String : Any]`

Returns a dictionary of the most recent fetched or saved values of the managed
object for the properties of the specified keys.

`func prepareForDeletion()`

Provides an opportunity to add code into the life cycle of the managed object
before deleting it.

`func willSave()`

Provides an opportunity to add code into the life cycle of the managed object
before saving it.

`func didSave()`

Provides an opportunity to add code into the life cycle of the managed object
after the managed object’s context completes a save operation.

`func willTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
before converting it to a fault.

`func didTurnIntoFault()`

Provides an opportunity to add code into the life cycle of the managed object
after converting it to a fault.

`class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>`

Returns an initialized fetch request with the entity this subclass represents.

`var objectWillChange: ObservableObjectPublisher`

A publisher that emits before the object changes.

Instance Method

# value(forKey:)

Returns the value for the property specified by `key`.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func value(forKey key: String) -> Any?

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Return Value

The value of the property specified by `key`.

## Discussion

If `key` is not a property defined by the model, the method raises an
exception. This method is overridden by `NSManagedObject` to access the
managed object’s generic dictionary storage unless the receiver’s class
explicitly provides key-value coding compliant accessor methods for `key`.

Important

You must not override this method.

## See Also

### Supporting Key-Value Coding

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

Instance Method

# setValue(_:forKey:)

Sets the specified property of the managed object to the specified value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setValue(
        _ value: Any?,
        forKey key: String
    )

##  Parameters

`value`

    

The new value for the property specified by `key`.

`key`

    

The name of one of the receiver's properties.

## Discussion

If `key` is not a property defined by the model, the method raises an
exception. If `key` identifies a to-one relationship, relates the object
specified by `value` to the receiver, unrelating the previously related object
if there was one. Given a collection object and a key that identifies a to-
many relationship, relates the objects contained in the collection to the
receiver, unrelating previously related objects if there were any.

This method is overridden by `NSManagedObject` to access the managed object’s
generic dictionary storage unless the receiver’s class explicitly provides
key-value coding compliant accessor methods for `key`.

Important

You must not override this method.

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

Instance Method

# primitiveValue(forKey:)

Returns the value for the specified property from the managed object’s private
internal storage .

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func primitiveValue(forKey key: String) -> Any?

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Return Value

The value of the property specified by `key`. Returns `nil` if no value has
been set.

## Discussion

This method does not invoke the access notification methods
(`willAccessValue(forKey:)` and `didAccessValue(forKey:)`). This method is
used primarily by subclasses that implement custom accessor methods that need
direct access to the receiver’s private storage.

### Special Considerations

Subclasses should not override this method.

The following points also apply:

  * Primitive accessor methods are only supported on _modeled_ properties. If you invoke a primitive accessor on an unmodeled property, it will instead operate upon a random modeled property. (The debug libraries and frameworks (available from Apple Developer Website) have assertions to test for passing unmodeled keys to these methods.)

  * You are strongly encouraged to use the dynamically-generated accessors rather than using this method directly (for example, `primitiveName:` instead of `primitiveValueForKey:@"name"`). The dynamic accessors are much more efficient, and allow for compile-time checking.

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`mutableSetValueForKey:`

Returns a mutable set that provides read-write access to the unordered to-many
relationship specified by a given key.

Instance Method

# setPrimitiveValue(_:forKey:)

Sets the value of a given property in the managed object's private internal
storage.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func setPrimitiveValue(
        _ value: Any?,
        forKey key: String
    )

##  Parameters

`value`

    

The new value for the property specified by `key`.

`key`

    

The name of one of the receiver's properties.

## Discussion

Sets in the receiver’s private internal storage the value of the property
specified by `key` to `value`. If `key` identifies a to-one relationship,
relates the object specified by `value` to the receiver, unrelating the
previously related object if there was one. Given a collection object and a
key that identifies a to-many relationship, relates the objects contained in
the collection to the receiver, unrelating previously related objects if there
were any.

This method does not invoke the change notification methods
(`willChangeValue(forKey:)` and `didChangeValue(forKey:)`). It is typically
used by subclasses that implement custom accessor methods that need direct
access to the receiver’s private internal storage. It is also used by the Core
Data framework to initialize the receiver with values from a persistent store
or to restore a value from a snapshot.

### Special Considerations

You must not override this method.

You should typically use this method only to modify attributes (usually
transient), not relationships. If you try to set a to-many relationship to a
new `NSMutableSet` object, it will (eventually) fail. In the unusual event
that you need to modify a relationship using this method, you first get the
existing set using `primitiveValueForKey:` (ensure the method does not return
`nil`), create a mutable copy, and then modify the copy—as illustrated in the
following example:

If the relationship is bi-directional (that is, if an inverse relationship is
specified) then you are also responsible for maintaining the inverse
relationship (regardless of cardinality)—in contrast with Core Data's normal
behavior described in Using Managed Objects.

The following points also apply:

  * Primitive accessor methods are only supported on _modeled_ properties. If you invoke a primitive accessor on an unmodeled property, it will instead operate upon a random modeled property. (The debug libraries and frameworks from (available from the Apple Developer Website) have assertions to test for passing unmodeled keys to these methods.)

  * You are strongly encouraged to use the dynamically-generated accessors rather than using this method directly (for example, `setPrimitiveName:` instead of `setPrimitiveValue:newName forKey:@"name"`). The dynamic accessors are much more efficient, and allow for compile-time checking.

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]`

Returns the object IDs for all of the managed objects that are in the named
relationship.

### Related Documentation

`func awakeFromFetch()`

Provides an opportunity to add code into the life cycle of the managed object
when fufilling it from a fault.

`mutableSetValueForKey:`

Returns a mutable set that provides read-write access to the unordered to-many
relationship specified by a given key.

Instance Method

# objectIDs(forRelationshipNamed:)

Returns the object IDs for all of the managed objects that are in the named
relationship.

iOS 8.3+  iPadOS 8.3+  macOS 10.11+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func objectIDs(forRelationshipNamed key: String) -> [NSManagedObjectID]

## See Also

### Supporting Key-Value Coding

`func value(forKey: String) -> Any?`

Returns the value for the property specified by `key`.

`func setValue(Any?, forKey: String)`

Sets the specified property of the managed object to the specified value.

`func primitiveValue(forKey: String) -> Any?`

Returns the value for the specified property from the managed object’s private
internal storage .

`func setPrimitiveValue(Any?, forKey: String)`

Sets the value of a given property in the managed object's private internal
storage.

Instance Method

# validateValue(_:forKey:)

Validates a property value for a given key.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateValue(
        _ value: AutoreleasingUnsafeMutablePointer<AnyObject?>,
        forKey key: String
    ) throws

##  Parameters

`value`

    

A pointer to an object.

`key`

    

The name of one of the receiver's properties.

`error`

    

If `value` is not a valid value for `key` (and cannot be coerced), upon return
contains an instance of `NSError` that describes the problem.

## Return Value

`true` if `value` is a valid value for `key` (or if `value` can be coerced
into a valid value for `key`), otherwise `false`.

## Discussion

This method is responsible for two things: coercing the value into an
appropriate type for the object, and validating it according to the object’s
rules.

The default implementation provided by `NSManagedObject` consults the object’s
entity description to coerce the value and to check for basic errors, such as
a null value when that isn’t allowed and the length of strings when a field
width is specified for the attribute. It then searches for a method of the
form `validate<Key>:error:` and invokes it if it exists.

You can implement methods of the form `validate<Key>:error:` to perform
validation that is not possible using the constraints available in the
property description. If it finds an unacceptable value, your validation
method should return `false` and in `error` an `NSError` object that describes
the problem. For more details, see Managed Object Validation. For inter-
property validation (to check for combinations of values that are invalid),
see `validateForUpdate()` and related methods.

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Instance Method

# validateForDelete()

Determines whether the managed object can be deleted in its current state.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateForDelete() throws

##  Parameters

`error`

    

If the receiver cannot be deleted in its current state, upon return contains
an instance of `NSError` that describes the problem.

## Return Value

`true` if the receiver can be deleted in its current state, otherwise `false`.

## Discussion

An object cannot be deleted if it has a relationship has a “deny” delete rule
and that relationship has a destination object.

`NSManagedObject`’s implementation sends the receiver’s entity description a
message which performs basic checking based on the presence or absence of
values.

Important

Subclasses should invoke super’s implementation before performing their own
validation, and should combine any error returned by super’s implementation
with their own (see Managed Object Validation).

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Instance Method

# validateForInsert()

Determines whether the managed object can be inserted in its current state.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateForInsert() throws

##  Parameters

`error`

    

If the receiver cannot be inserted in its current state, upon return contains
an instance of `NSError` that describes the problem.

## Return Value

`true` if the receiver can be inserted in its current state, otherwise
`false`.

## Discussion

Subclasses should invoke super’s implementation before performing their own
validation, and should combine any error returned by super’s implementation
with their own (see Managed Object Validation).

### Discussion

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Instance Method

# validateForUpdate()

Determines whether the managed object's current state is valid.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func validateForUpdate() throws

##  Parameters

`error`

    

If the receiver's current state is invalid, upon return contains an instance
of `NSError` that describes the problem.

## Return Value

`true` if the receiver's current state is valid, otherwise `false`.

## Discussion

`NSManagedObject`’s implementation iterates through all of the receiver’s
properties validating each in turn. If this results in more than one error,
the `userInfo` dictionary in the `NSError` returned in `error` contains a key
`NSDetailedErrorsKey`; the corresponding value is an array containing the
individual validation errors. If you pass `NULL` as the error, validation will
abort after the first failure.

Important

Subclasses should invoke super’s implementation before performing their own
validation, and should combine any error returned by super’s implementation
with their own (see Managed Object Validation).

Handling Errors in Swift:

In Swift, this method returns `Void` and is marked with the `throws` keyword
to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the
`catch` clauses of a `do` statement, as described in Error Handling in The
Swift Programming Language and `About Imported Cocoa Error Parameters`.

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationKeyErrorKey

The error key for the attribute that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationKeyErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationObjectErrorKey

The error key for the object that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationObjectErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationPredicateErrorKey

The error key for the predicate that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationPredicateErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationValueErrorKey: String`

The error key for the value that failed to validate.

Global Variable

# NSValidationValueErrorKey

The error key for the value that failed to validate.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    let NSValidationValueErrorKey: String

## See Also

### Managing Data Validation

`func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey:
String)`

Validates a property value for a given key.

`func validateForDelete()`

Determines whether the managed object can be deleted in its current state.

`func validateForInsert()`

Determines whether the managed object can be inserted in its current state.

`func validateForUpdate()`

Determines whether the managed object's current state is valid.

API Reference

Validation error codes

Error codes relating to the validation of managed objects.

`let NSValidationKeyErrorKey: String`

The error key for the attribute that failed to validate.

`let NSValidationObjectErrorKey: String`

The error key for the object that failed to validate.

`let NSValidationPredicateErrorKey: String`

The error key for the predicate that failed to validate.

Instance Method

# didAccessValue(forKey:)

Provides support for key-value observing access notification.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didAccessValue(forKey key: String?)

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Discussion

Together with `willAccessValue(forKey:)`, this method is used to fire faults,
to maintain inverse relationships, and so on. Each read access must be wrapped
in this method pair (in the same way that each write access must be wrapped in
the `willChangeValueForKey:`/`didChangeValueForKey:` method pair). In the
default implementation of `NSManagedObject` these methods are invoked for you
automatically. If, say, you create a custom subclass that uses explicit
instance variables, you must invoke them yourself, as in the following
example.

## See Also

### Supporting Key-Value Observing

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# observationInfo()

Returns the observation info of the managed object.

macOS 10.4+  Mac Catalyst 13.1+

    
    
    func observationInfo() -> UnsafeMutableRawPointer?

## Return Value

The observation info of the receiver.

## Discussion

For more about key-value observation, see Key-Value Observing Programming
Guide.

Important

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# setObservationInfo(_:)

Sets the observation info of the managed object.

macOS 10.4+  Mac Catalyst 13.1+

    
    
    func setObservationInfo(_ inObservationInfo: UnsafeMutableRawPointer?)

##  Parameters

`value`

    

The new observation info for the receiver.

## Discussion

For more about observation information, see Key-Value Observing Programming
Guide.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# willAccessValue(forKey:)

Provides support for key-value observing access notification.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willAccessValue(forKey key: String?)

##  Parameters

`key`

    

The name of one of the receiver's properties.

## Discussion

See `didAccessValue(forKey:)` for more details. You can invoke this method
with the `key` value of `nil` to ensure that a fault has been fired, as
illustrated by the following example.

    
    
    [aManagedObject willAccessValueForKey:nil];
    

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# didChangeValue(forKey:)

Provides an opportunity to respond when a value of a given property has
changed.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didChangeValue(forKey key: String)

##  Parameters

`key`

    

The name of the property that changed.

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# didChangeValue(forKey:withSetMutation:using:)

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func didChangeValue(
        forKey inKey: String,
        withSetMutation inMutationKind: NSKeyValueSetMutationKind,
        using inObjects: Set<AnyHashable>
    )

##  Parameters

`inKey`

    

The name of a property that is a to-many relationship.

`inMutationKind`

    

The type of change that was made.

`inObjects`

    

The objects that were involved in the change (see
`NSKeyValueSetMutationKind`).

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# willChangeValue(forKey:)

Provides an opportunity to respond when a value of a given property is about
to change.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willChangeValue(forKey key: String)

##  Parameters

`key`

    

The name of the property that will change.

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

Instance Method

# willChangeValue(forKey:withSetMutation:using:)

Provides an opportunity to respond when a change is about to be made to a
specified to-many relationship.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.1+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    func willChangeValue(
        forKey inKey: String,
        withSetMutation inMutationKind: NSKeyValueSetMutationKind,
        using inObjects: Set<AnyHashable>
    )

##  Parameters

`inKey`

    

The name of a property that is a to-many relationship

`inMutationKind`

    

The type of change that will be made.

`inObjects`

    

The objects that were involved in the change (see
`NSKeyValueSetMutationKind`).

## Discussion

For more details, see Key-Value Observing Programming Guide.

You must not override this method.

## See Also

### Supporting Key-Value Observing

`func didAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func observationInfo() -> UnsafeMutableRawPointer?`

Returns the observation info of the managed object.

`func setObservationInfo(UnsafeMutableRawPointer?)`

Sets the observation info of the managed object.

`func willAccessValue(forKey: String?)`

Provides support for key-value observing access notification.

`func didChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property has
changed.

`func didChangeValue(forKey: String, withSetMutation:
NSKeyValueSetMutationKind, using: Set<AnyHashable>)`

Provides an opportunity to respond when a change was made to a specified to-
many relationship.

`func willChangeValue(forKey: String)`

Provides an opportunity to respond when a value of a given property is about
to change.

