import { applicant } from "./applicant";

export interface ticket {
    Description: string;
    Subject: string;
    Applicant: applicant
}

export class ticket implements ticket {

}