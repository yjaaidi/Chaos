Feature: update disruption

   Scenario: I can update the wording of a cause
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | None                   | None                 |

        When I put to "/disruptions/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"reference":"foobarz","publication_period": {"begin":"2014-06-24T13:35:00Z","end":"2014-07-08T18:00:00Z"}}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.publication_period.begin" should be "2014-06-24T13:35:00Z"
        And the field "disruption.publication_period.end" should be "2014-07-08T18:00:00Z"
