Feature: Create export

  Background:
        I fill in header "X-Customer-Id" with "test"
        I fill in header "Authorization" with "d5b0148c-36f4-443c-9818-1f2f74a00be0"

    Scenario: we cannot create a property without header X-Customer-Id
        I remove header "X-Customer-Id"
        When I post to "/impacts/exports" with:
        """
        {"start_date": "2014-04-02T23:52:12Z", "end_date": "2014-04-04T23:52:12Z"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "The parameter X-Customer-Id does not exist in the header"

    Scenario: we cannot create an impact export without data
        Given I have the following clients in my database:
        | client_code | created_at          | updated_at          | id                                   |
        | test        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        When I post to "/impacts/exports" with:
        """

        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "None is not of type 'object'"


    Scenario: we cannot create a impact export without 'start_date' and 'end_date' values
        Given I have the following clients in my database:
        | client_code | created_at          | updated_at          | id                                   |
        | test        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        When I post to "/impacts/exports" with:
        """
        {}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "'start_date' is a required property"

    Scenario: we cannot create a property without 'end_date' data
        Given I have the following clients in my database:
        | client_code | created_at          | updated_at          | id                                   |
        | test        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        When I post to "/impacts/exports" with:
        """
        {"start_date": "2014-04-02T23:52:12Z"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "'end_date' is a required property"

    Scenario: we cannot create a property without 'start_date' data
        Given I have the following clients in my database:
        | client_code | created_at          | updated_at          | id                                   |
        | test        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        When I post to "/impacts/exports" with:
        """
        {"end_date": "2014-04-02T23:52:12Z"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "'start_date' is a required property"

    Scenario: create a impact export which doesn't exist in database
        Given I have the following clients in my database:
        | client_code | created_at          | updated_at          | id                                   |
        | test        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        When I post to "/impacts/exports" with:
        """
        {"start_date": "2014-04-02T23:52:12Z", "end_date": "2014-04-04T23:52:12Z"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "export" should have a size of 7
        And the field "export.id" should be an id
        And the field "export.status" should be "waiting"
        And the field "export.process_start_date" should be null
        And the field "export.start_date" should be "2014-04-02T23:52:12Z"
        And the field "export.end_date" should be "2014-04-04T23:52:12Z"
        And the field "property.created_at" should be not null

    Scenario: create a impact export which exist in database
        Given I have the following clients in my database:
            | client_code   | created_at          | id                                   |
            | test          | 2014-04-02T23:52:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following exports in my database:
            | id                                   | client_id                            | status  | created_at          | process_start_date  | start_date          | end_date            | file_path                                           |
            | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | done    | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 2014-03-01T00:00:00 | 2014-04-01T00:00:00 | /tmp/5/export_2014-03-01T00-00_2014-04-01T00-00.csv |
            | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | working | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 2014-02-01T00:00:00 | 2014-03-01T00:00:00 | /tmp/5/export_2014-02-01T00-00_2014-03-01T00-00.csv |
        When I post to "/impacts/exports" with:
        """
        {"start_date": "2014-03-01T00:00:00Z", "end_date": "2014-04-01T00:00:00Z"}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "export" should have a size of 7
        And the field "export.id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"


    Scenario: create a impact export which exist in database
        Given I have the following clients in my database:
            | client_code   | created_at          | id                                   |
            | test          | 2014-04-02T23:52:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |
        Given I have the following exports in my database:
            | id                                   | client_id                            | status  | created_at          | process_start_date  | start_date          | end_date            | file_path                                           |
            | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | error    | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 2014-03-01T00:00:00 | 2014-04-01T00:00:00 | /tmp/5/export_2014-03-01T00-00_2014-04-01T00-00.csv |
        When I post to "/impacts/exports" with:
        """
        {"start_date": "2014-03-01T00:00:00Z", "end_date": "2014-04-01T00:00:00Z"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "export" should have a size of 7
        And the field "export.id" should be an id
        And the field "export.status" should be "waiting"
        And the field "export.process_start_date" should be null
        And the field "export.start_date" should be "2014-03-01T00:00:00Z"
        And the field "export.end_date" should be "2014-04-01T00:00:00Z"
        And the field "property.created_at" should be not null
