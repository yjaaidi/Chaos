Feature: list disruptions with pager

    Scenario: Use pager to display disruptions
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 |
        When I get "/disruptions"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 3
        And the field "meta" should exist
        And the field "meta.pagination.items_per_page" should be 20
        And the field "meta.pagination.items_on_page" should be 3
        And the field "meta.pagination.start_page" should be 1


    Scenario: Use pager to display disruptions with parameters (start_page=1)
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 |
        When I get "/disruptions?start_page=1&items_per_page=2"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 2
        And the field "meta" should exist
        And the field "meta.pagination.items_per_page" should be 2
        And the field "meta.pagination.items_on_page" should be 2
        And the field "meta.pagination.start_page" should be 1
        And the field "meta.pagination.total_result" should be 3
        And the field "meta.pagination.prev.href" should be null
        And the field "meta.pagination.first.href" should be "http://localhost/disruptions?start_page=1&items_per_page=2"
        And the field "meta.pagination.next.href" should be "http://localhost/disruptions?start_page=2&items_per_page=2"
        And the field "meta.pagination.last.href" should be "http://localhost/disruptions?start_page=2&items_per_page=2"

    Scenario: Use pager to display disruptions with parameters (start_page=2)
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 |
        When I get "/disruptions?start_page=2&items_per_page=2"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "meta" should exist
        And the field "meta.pagination.items_per_page" should be 2
        And the field "meta.pagination.items_on_page" should be 1
        And the field "meta.pagination.start_page" should be 2
        And the field "meta.pagination.total_result" should be 3
        And the field "meta.pagination.prev.href" should be "http://localhost/disruptions?start_page=1&items_per_page=2"
        And the field "meta.pagination.first.href" should be "http://localhost/disruptions?start_page=1&items_per_page=2"
        And the field "meta.pagination.next.href" should be null
        And the field "meta.pagination.last.href" should be "http://localhost/disruptions?start_page=2&items_per_page=2"