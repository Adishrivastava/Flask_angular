import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ApiService {

  private apiRoot = 'http://localhost:5000/';

  constructor(private http: HttpClient) { }


  getMain() {
    return this.http.get(this.apiRoot.concat(''));
  }
}