// types.ts
import { ICreateUserDTO } from './dtos/ICreateUserDTO';
import { IUpdateUserDTO } from './dtos/IUpdateUserDTO';

export interface IUser {
  id: string;
  name: string;
  email: string;
  created_at: Date;
  updated_at: Date;
}

export interface ICreateUserDTO {
  name: string;
  email: string;
  password: string;
}

export interface IUpdateUserDTO {
  name?: string;
  email?: string;
  password?: string;
}

export interface ILoginUserDTO {
  email: string;
  password: string;
}