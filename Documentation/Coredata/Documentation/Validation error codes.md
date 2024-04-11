Global Variable

# NSCoreDataError

An error code that indicates a nonspecific Core Data error.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSCoreDataError: Int { get }

## See Also

### Error codes

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSEntityMigrationPolicyError

An error code that indicates a migration failure during processing of an
entity migration policy.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSEntityMigrationPolicyError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSExternalRecordImportError

Error code to denote a general error encountered while importing external
records.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSExternalRecordImportError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSInferredMappingModelError

Error code to denote a problem with the creation of an inferred mapping model.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSInferredMappingModelError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectConstraintMergeError

Error code to denote a problem with the merging of instances of a managed
object.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectConstraintMergeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectConstraintValidationError

Error code to denote a problem with the validation of a managed object.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectConstraintValidationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectContextLockingError

Error code to denote an inability to acquire a lock in a managed object
context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectContextLockingError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectExternalRelationshipError

Error code to denote that an object being saved has a relationship containing
an object from another store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectExternalRelationshipError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectMergeError

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectMergeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectModelReferenceNotFoundError

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var NSManagedObjectModelReferenceNotFoundError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectReferentialIntegrityError

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectReferentialIntegrityError: Int { get }

## Discussion

The store is accessible, but the object corresponding to the fault cannot be
found.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectValidationError

Error code to denote a generic validation error.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectValidationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationCancelledError

Error code to denote that migration failed due to manual cancellation.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationCancelledError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationConstraintViolationError

Error code to denote a problem with the validation of a managed object during
a migration.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationConstraintViolationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationError

Error code to denote a general migration error.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationManagerDestinationStoreError

Error code to denote that migration failed due to a problem with the
destination data store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationManagerDestinationStoreError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationManagerSourceStoreError

Error code to denote that migration failed due to a problem with the source
data store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationManagerSourceStoreError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationMissingMappingModelError

Error code to denote that migration failed due to a missing mapping model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationMissingMappingModelError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationMissingSourceModelError

Error code to denote that migration failed due to a missing source data model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationMissingSourceModelError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentHistoryTokenExpiredError

Error code to denote that the persistent history token has expired.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.0+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var NSPersistentHistoryTokenExpiredError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreCoordinatorLockingError

Error code to denote an inability to acquire a lock in a persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreCoordinatorLockingError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreIncompatibleSchemaError

Error code to denote that a persistent store returned an error for a save
operation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreIncompatibleSchemaError: Int { get }

## Discussion

This code pertains to database level errors such as a missing table.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreIncompatibleVersionHashError

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreIncompatibleVersionHashError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreIncompleteSaveError

Error code to denote that one or more of the stores returned an error during a
save operations.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreIncompleteSaveError: Int { get }

## Discussion

The stores or objects that failed are in the corresponding user info
dictionary of the `NSError` object.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreInvalidTypeError

Error code to denote an unknown persistent store type/format/version.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreInvalidTypeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreOpenError

Error code to denote an error occurred while attempting to open a persistent
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreOpenError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreOperationError

Error code to denote that a persistent store operation failed.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreOperationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreSaveConflictsError

Error code to denote that an unresolved merge conflict was encountered during
a save. .

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreSaveConflictsError: Int { get }

## Discussion

The `NSError` object’s user info dictionary contains the key
`NSPersistentStoreSaveConflictsErrorKey`.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreSaveError

Error code to denote that a persistent store returned an error for a save
operation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreSaveError: Int { get }

## Discussion

This code pertains to errors such as permissions problems.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreTimeoutError

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreTimeoutError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreTypeMismatchError

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreTypeMismatchError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreUnsupportedRequestTypeError

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreUnsupportedRequestTypeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSSQLiteError

Error code to denote a general SQLite error.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSSQLiteError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSStagedMigrationBackwardMigrationError

An error code that indicates a failed migration because of an attempt to
migrate backward.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var NSStagedMigrationBackwardMigrationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSStagedMigrationFrameworkVersionMismatchError

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var NSStagedMigrationFrameworkVersionMismatchError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationInvalidURIError

Error code to denote a problem with the validation of a URI property.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.0+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var NSValidationInvalidURIError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationMultipleErrorsError

Error code to denote an error containing multiple validation errors.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationMultipleErrorsError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationMissingMandatoryPropertyError

Error code for a non-optional property with a nil value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationMissingMandatoryPropertyError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationRelationshipLacksMinimumCountError

Error code to denote a to-many relationship with too few destination objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationRelationshipLacksMinimumCountError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationRelationshipExceedsMaximumCountError

Error code to denote a bounded to-many relationship with too many destination
objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationRelationshipExceedsMaximumCountError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationRelationshipDeniedDeleteError

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationRelationshipDeniedDeleteError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationNumberTooLargeError

Error code to denote some numerical value is too large.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationNumberTooLargeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationNumberTooSmallError

Error code to denote some numerical value is too small.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationNumberTooSmallError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationDateTooLateError

Error code to denote some date value is too late.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationDateTooLateError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationDateTooSoonError

Error code to denote some date value is too soon.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationDateTooSoonError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationInvalidDateError

Error code to denote some date value fails to match date pattern.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationInvalidDateError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationStringTooLongError

Error code to denote some string value is too long.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationStringTooLongError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationStringTooShortError

Error code to denote some string value is too short.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationStringTooShortError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationStringPatternMatchingError

Error code to denote some string value fails to match some pattern.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationStringPatternMatchingError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

Global Variable

# NSCoreDataError

An error code that indicates a nonspecific Core Data error.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSCoreDataError: Int { get }

## See Also

### Error codes

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSEntityMigrationPolicyError

An error code that indicates a migration failure during processing of an
entity migration policy.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSEntityMigrationPolicyError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSExternalRecordImportError

Error code to denote a general error encountered while importing external
records.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSExternalRecordImportError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSInferredMappingModelError

Error code to denote a problem with the creation of an inferred mapping model.

iOS 3.0+  iPadOS 3.0+  macOS 10.6+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSInferredMappingModelError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectConstraintMergeError

Error code to denote a problem with the merging of instances of a managed
object.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectConstraintMergeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectConstraintValidationError

Error code to denote a problem with the validation of a managed object.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectConstraintValidationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectContextLockingError

Error code to denote an inability to acquire a lock in a managed object
context.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectContextLockingError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectExternalRelationshipError

Error code to denote that an object being saved has a relationship containing
an object from another store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectExternalRelationshipError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectMergeError

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectMergeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectModelReferenceNotFoundError

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var NSManagedObjectModelReferenceNotFoundError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectReferentialIntegrityError

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectReferentialIntegrityError: Int { get }

## Discussion

The store is accessible, but the object corresponding to the fault cannot be
found.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSManagedObjectValidationError

Error code to denote a generic validation error.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSManagedObjectValidationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationCancelledError

Error code to denote that migration failed due to manual cancellation.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationCancelledError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationConstraintViolationError

Error code to denote a problem with the validation of a managed object during
a migration.

iOS 9.0+  iPadOS 9.0+  macOS 10.11+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationConstraintViolationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationError

Error code to denote a general migration error.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationManagerDestinationStoreError

Error code to denote that migration failed due to a problem with the
destination data store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationManagerDestinationStoreError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationManagerSourceStoreError

Error code to denote that migration failed due to a problem with the source
data store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationManagerSourceStoreError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationMissingMappingModelError

Error code to denote that migration failed due to a missing mapping model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationMissingMappingModelError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSMigrationMissingSourceModelError

Error code to denote that migration failed due to a missing source data model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSMigrationMissingSourceModelError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentHistoryTokenExpiredError

Error code to denote that the persistent history token has expired.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.0+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var NSPersistentHistoryTokenExpiredError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreCoordinatorLockingError

Error code to denote an inability to acquire a lock in a persistent store.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreCoordinatorLockingError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreIncompatibleSchemaError

Error code to denote that a persistent store returned an error for a save
operation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreIncompatibleSchemaError: Int { get }

## Discussion

This code pertains to database level errors such as a missing table.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreIncompatibleVersionHashError

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreIncompatibleVersionHashError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreIncompleteSaveError

Error code to denote that one or more of the stores returned an error during a
save operations.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreIncompleteSaveError: Int { get }

## Discussion

The stores or objects that failed are in the corresponding user info
dictionary of the `NSError` object.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreInvalidTypeError

Error code to denote an unknown persistent store type/format/version.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreInvalidTypeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreOpenError

Error code to denote an error occurred while attempting to open a persistent
store.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreOpenError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreOperationError

Error code to denote that a persistent store operation failed.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreOperationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreSaveConflictsError

Error code to denote that an unresolved merge conflict was encountered during
a save. .

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreSaveConflictsError: Int { get }

## Discussion

The `NSError` object’s user info dictionary contains the key
`NSPersistentStoreSaveConflictsErrorKey`.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreSaveError

Error code to denote that a persistent store returned an error for a save
operation.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreSaveError: Int { get }

## Discussion

This code pertains to errors such as permissions problems.

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreTimeoutError

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreTimeoutError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreTypeMismatchError

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreTypeMismatchError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSPersistentStoreUnsupportedRequestTypeError

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

iOS 5.0+  iPadOS 5.0+  macOS 10.7+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSPersistentStoreUnsupportedRequestTypeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSSQLiteError

Error code to denote a general SQLite error.

iOS 3.0+  iPadOS 3.0+  macOS 10.5+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSSQLiteError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSStagedMigrationBackwardMigrationError

An error code that indicates a failed migration because of an attempt to
migrate backward.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var NSStagedMigrationBackwardMigrationError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSStagedMigrationFrameworkVersionMismatchError

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var NSStagedMigrationFrameworkVersionMismatchError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationInvalidURIError

Error code to denote a problem with the validation of a URI property.

iOS 11.0+  iPadOS 11.0+  macOS 10.13+  Mac Catalyst 13.0+  tvOS 11.0+  watchOS
4.0+  visionOS 1.0+

    
    
    var NSValidationInvalidURIError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationMultipleErrorsError

Error code to denote an error containing multiple validation errors.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationMultipleErrorsError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationMissingMandatoryPropertyError

Error code for a non-optional property with a nil value.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationMissingMandatoryPropertyError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationRelationshipLacksMinimumCountError

Error code to denote a to-many relationship with too few destination objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationRelationshipLacksMinimumCountError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationRelationshipExceedsMaximumCountError

Error code to denote a bounded to-many relationship with too many destination
objects.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationRelationshipExceedsMaximumCountError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationRelationshipDeniedDeleteError

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationRelationshipDeniedDeleteError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationNumberTooLargeError

Error code to denote some numerical value is too large.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationNumberTooLargeError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationNumberTooSmallError

Error code to denote some numerical value is too small.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationNumberTooSmallError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationDateTooLateError

Error code to denote some date value is too late.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationDateTooLateError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationDateTooSoonError

Error code to denote some date value is too soon.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationDateTooSoonError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationInvalidDateError

Error code to denote some date value fails to match date pattern.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationInvalidDateError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationStringTooLongError

Error code to denote some string value is too long.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationStringTooLongError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationStringTooShortError

Error code to denote some string value is too short.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationStringTooShortError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringPatternMatchingError: Int`

Error code to denote some string value fails to match some pattern.

Global Variable

# NSValidationStringPatternMatchingError

Error code to denote some string value fails to match some pattern.

iOS 3.0+  iPadOS 3.0+  macOS 10.4+  Mac Catalyst 13.0+  tvOS 9.0+  watchOS
2.0+  visionOS 1.0+

    
    
    var NSValidationStringPatternMatchingError: Int { get }

## See Also

### Error codes

`var NSCoreDataError: Int`

An error code that indicates a nonspecific Core Data error.

`var NSEntityMigrationPolicyError: Int`

An error code that indicates a migration failure during processing of an
entity migration policy.

`var NSExternalRecordImportError: Int`

Error code to denote a general error encountered while importing external
records.

`var NSInferredMappingModelError: Int`

Error code to denote a problem with the creation of an inferred mapping model.

`var NSManagedObjectConstraintMergeError: Int`

Error code to denote a problem with the merging of instances of a managed
object.

`var NSManagedObjectConstraintValidationError: Int`

Error code to denote a problem with the validation of a managed object.

`var NSManagedObjectContextLockingError: Int`

Error code to denote an inability to acquire a lock in a managed object
context.

`var NSManagedObjectExternalRelationshipError: Int`

Error code to denote that an object being saved has a relationship containing
an object from another store.

`var NSManagedObjectMergeError: Int`

Error code to denote that a merge policy failed—Core Data is unable to
complete merging.

`var NSManagedObjectModelReferenceNotFoundError: Int`

An error code that indicates Core Data isn’t able to find or instantiate the
referenced object model.

`var NSManagedObjectReferentialIntegrityError: Int`

Error code to denote an attempt to fire a fault pointing to an object that
does not exist.

`var NSManagedObjectValidationError: Int`

Error code to denote a generic validation error.

`var NSMigrationCancelledError: Int`

Error code to denote that migration failed due to manual cancellation.

`var NSMigrationConstraintViolationError: Int`

Error code to denote a problem with the validation of a managed object during
a migration.

`var NSMigrationError: Int`

Error code to denote a general migration error.

`var NSMigrationManagerDestinationStoreError: Int`

Error code to denote that migration failed due to a problem with the
destination data store.

`var NSMigrationManagerSourceStoreError: Int`

Error code to denote that migration failed due to a problem with the source
data store.

`var NSMigrationMissingMappingModelError: Int`

Error code to denote that migration failed due to a missing mapping model.

`var NSMigrationMissingSourceModelError: Int`

Error code to denote that migration failed due to a missing source data model.

`var NSPersistentHistoryTokenExpiredError: Int`

Error code to denote that the persistent history token has expired.

`var NSPersistentStoreCoordinatorLockingError: Int`

Error code to denote an inability to acquire a lock in a persistent store.

`var NSPersistentStoreIncompatibleSchemaError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreIncompatibleVersionHashError: Int`

Error code to denote that entity version hashes in the store are incompatible
with the current managed object model.

`var NSPersistentStoreIncompleteSaveError: Int`

Error code to denote that one or more of the stores returned an error during a
save operations.

`var NSPersistentStoreInvalidTypeError: Int`

Error code to denote an unknown persistent store type/format/version.

`var NSPersistentStoreOpenError: Int`

Error code to denote an error occurred while attempting to open a persistent
store.

`var NSPersistentStoreOperationError: Int`

Error code to denote that a persistent store operation failed.

`var NSPersistentStoreSaveConflictsError: Int`

Error code to denote that an unresolved merge conflict was encountered during
a save. .

`var NSPersistentStoreSaveError: Int`

Error code to denote that a persistent store returned an error for a save
operation.

`var NSPersistentStoreTimeoutError: Int`

Error code to denote that Core Data failed to connect to a persistent store
within the time specified by `NSPersistentStoreTimeoutOption`.

`var NSPersistentStoreTypeMismatchError: Int`

Error code returned by a persistent store coordinator if a store is accessed
that does not match the specified type.

`var NSPersistentStoreUnsupportedRequestTypeError: Int`

Error code to denote that an `NSPersistentStore` subclass was passed a request
(an instance of `NSPersistentStoreRequest`) that it did not understand.

`var NSSQLiteError: Int`

Error code to denote a general SQLite error.

`var NSStagedMigrationBackwardMigrationError: Int`

An error code that indicates a failed migration because of an attempt to
migrate backward.

`var NSStagedMigrationFrameworkVersionMismatchError: Int`

An error code that indicates a failed migration because the persistent store’s
metadata doesn’t support staged lightweight migrations.

`var NSValidationInvalidURIError: Int`

Error code to denote a problem with the validation of a URI property.

`var NSValidationMultipleErrorsError: Int`

Error code to denote an error containing multiple validation errors.

`var NSValidationMissingMandatoryPropertyError: Int`

Error code for a non-optional property with a nil value.

`var NSValidationRelationshipLacksMinimumCountError: Int`

Error code to denote a to-many relationship with too few destination objects.

`var NSValidationRelationshipExceedsMaximumCountError: Int`

Error code to denote a bounded to-many relationship with too many destination
objects.

`var NSValidationRelationshipDeniedDeleteError: Int`

Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is
non-empty.

`var NSValidationNumberTooLargeError: Int`

Error code to denote some numerical value is too large.

`var NSValidationNumberTooSmallError: Int`

Error code to denote some numerical value is too small.

`var NSValidationDateTooLateError: Int`

Error code to denote some date value is too late.

`var NSValidationDateTooSoonError: Int`

Error code to denote some date value is too soon.

`var NSValidationInvalidDateError: Int`

Error code to denote some date value fails to match date pattern.

`var NSValidationStringTooLongError: Int`

Error code to denote some string value is too long.

`var NSValidationStringTooShortError: Int`

Error code to denote some string value is too short.

